import re
from datetime import datetime
from fpdf import FPDF
import PyPDF2
from tkinter import Tk, filedialog, messagebox
from analisa_perfil_e_curriculo.src.analisa_perfil_e_curriculo.crew import AnalisaPerfilECurriculo
from dotenv import load_dotenv
import unicodedata

load_dotenv()

def abrir_pdf():
    root = Tk()
    root.withdraw()

    caminhos_arquivos = filedialog.askopenfilenames(
        title="Selecione os arquivos",
        filetypes=(("PDFs", "*.pdf"), ("Todos", "*.*"))
    )

    if not caminhos_arquivos:
        messagebox.showinfo("Informação", "Nenhum arquivo selecionado!")
        return

    resultados_gerais = []

    for arquivo in caminhos_arquivos:
        print(f"\nProcessando arquivo: {arquivo}")
        try:
            with open(arquivo, "rb") as file:
                leitor = PyPDF2.PdfReader(file)
                texto = "".join([pagina.extract_text() for pagina in leitor.pages])

                if not texto.strip():
                    raise ValueError("O PDF não contém texto extraível")

                print(f"Texto extraído (amostra): {texto[:200]}...")
                resultado = analise_feita_ia(texto)
                resultados_gerais.append(resultado)

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao processar {arquivo}: {str(e)}")

    root.destroy()

    # Após processar todos os currículos, gera o PDF único
    if resultados_gerais:
        conteudo_unico = "\n\n---\n\n".join(resultados_gerais)
        cria_pdf(conteudo_unico)


def analise_feita_ia(curriculos_texto):
    """Executa a crew e retorna o resultado como texto."""
    try:
        crew = AnalisaPerfilECurriculo()
        inputs = {'curriculos': curriculos_texto}
        print(f"\nInputs sendo passados para a crew: {inputs.keys()}")

        resultado = crew.crew().kickoff(inputs=inputs)
        return str(resultado)

    except Exception as e:
        messagebox.showerror("Erro na Análise", f"Falha na análise: {str(e)}")
        return f"Erro ao processar currículo: {str(e)}"


def limpar_texto(texto):
    # Substitui manualmente alguns caracteres comuns problemáticos
    texto = texto.replace('–', '-')  # en dash
    texto = texto.replace('“', '"').replace('”', '"')  # aspas
    texto = texto.replace('‘', "'").replace('’', "'")  # apóstrofos

    # Remove acentos e outros símbolos incompatíveis
    texto = unicodedata.normalize('NFKD', texto).encode('latin-1', 'ignore').decode('latin-1')
    return texto

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Arial", size=12)

    def add_markdown_line(self, line):
        # Cabeçalhos
        if line.startswith("### "):  # H3
            self.set_font("Arial", "B", 14)
            self.multi_cell(0, 10, line[4:])
            self.ln(1)
        elif line.startswith("#### "):  # H4
            self.set_font("Arial", "B", 12)
            self.multi_cell(0, 8, line[5:])
            self.ln(1)
        elif line.strip() == "***":  # Separador
            self.set_draw_color(180)
            self.cell(0, 5, "", ln=1, border="B")
            self.ln(2)
        else:
            # Negrito dentro da linha
            self.set_font("Arial", "", 12)
            # Substituir **texto** por texto em negrito
            parts = re.split(r"(\*\*.*?\*\*)", line)
            for part in parts:
                if part.startswith("**") and part.endswith("**"):
                    self.set_font("Arial", "B", 12)
                    self.write(6, part[2:-2])
                    self.set_font("Arial", "", 12)
                else:
                    self.write(6, part)
            self.ln(8)

def cria_pdf(conteudo):
    try:
        pdf = PDF()

        texto = str(conteudo).strip()
        linhas = texto.split('\n')

        for linha in linhas:
            if linha.strip() == "":
                pdf.ln(5)
                continue
            pdf.add_markdown_line(linha)

        nome_arquivo = f"Analise_Curriculo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(nome_arquivo)
        messagebox.showinfo("Sucesso", f"Análise salva em: {nome_arquivo}")

    except Exception as e:
        messagebox.showerror("Erro PDF", f"Falha ao gerar PDF: {str(e)}")
if __name__ == "__main__":
    abrir_pdf()
