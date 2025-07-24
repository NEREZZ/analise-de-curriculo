# Sistema de Análise de Currículos com CrewAI

## 📋 Visão Geral

Este projeto implementa um sistema automatizado de análise de currículos utilizando **CrewAI**, uma framework de IA multi-agente. O sistema avalia candidatos com base nos valores culturais da empresa, fornecendo análises precisas e feedback estruturado sobre a compatibilidade cultural dos perfis profissionais.

## 🎯 Objetivos

- **Automatizar** o processo de triagem de currículos
- **Avaliar** alinhamento cultural com os valores da empresa
- **Gerar** feedback construtivo e profissional
- **Otimizar** o tempo dos recrutadores focando em análises estratégicas
- **Produzir** relatórios estruturados em formato PDF

## 🏗️ Arquitetura do Sistema

### Estrutura Multi-Agente (CrewAI)

O sistema utiliza dois agentes especializados trabalhando em sequência:

#### 1. **RH Agent** (Especialista em Recrutamento)
- **Função**: Análise técnica e cultural dos currículos
- **Experiência**: 15+ anos em RH e recrutamento
- **Responsabilidades**:
  - Extrair informações relevantes dos currículos
  - Avaliar alinhamento com valores culturais da ARMS
  - Identificar até 3 principais compatibilidades
  - Classificar perfis profissionais

#### 2. **Comunicador Agent** (Formatador de Respostas)
- **Função**: Formatação e apresentação das análises
- **Responsabilidades**:
  - Melhorar apresentação visual das respostas
  - Preservar integralmente o conteúdo da análise
  - Garantir clareza e profissionalismo na comunicação

## 🎭 Valores Culturais da ARMS

O sistema avalia candidatos baseado em 5 valores fundamentais:

### 1. **Eficiência e Autonomia**
- Valorização da produtividade contínua
- Capacidade de trabalho independente
- Foco em automação inteligente

### 2. **Inovação Tecnológica**
- Experiência com IA generativa
- Conhecimento em engenharia de prompt
- Experiência com integrações via API

### 3. **Empoderamento das Equipes**
- Foco em pensamento estratégico
- Capacidade de crescimento profissional
- Habilidades de tomada de decisão

### 4. **Personalização e Flexibilidade**
- Abordagem centrada no cliente
- Capacidade de adaptação
- Experiência em co-criação de soluções

### 5. **Compromisso com Privacidade**
- Conhecimento em LGPD
- Responsabilidade digital
- Ética em proteção de dados

## 🛠️ Tecnologias Utilizadas

### Core Framework
- **CrewAI**: Framework de agentes de IA colaborativos
- **Python 3.x**: Linguagem principal do projeto

### Bibliotecas Principais
```python
crewai                 # Framework multi-agente
PyPDF2                # Extração de texto de PDFs
fpdf                  # Geração de relatórios PDF
tkinter               # Interface gráfica para seleção de arquivos
python-dotenv         # Gerenciamento de variáveis de ambiente
unicodedata           # Processamento de caracteres especiais
```

## 📁 Estrutura de Arquivos

```
projeto/
│
├── app.py                 # Interface principal e processamento
├── crew.py               # Configuração dos agentes CrewAI
├── agents.yaml           # Definição dos agentes
├── tasks.yaml            # Configuração das tarefas
├── .env                  # Variáveis de ambiente
└── report.md            # Saída gerada automaticamente
```

## ⚙️ Funcionamento do Sistema

### 1. **Seleção de Arquivos**
```python
def abrir_pdf():
    # Interface gráfica para seleção de PDFs
    # Suporta seleção múltipla de arquivos
```

### 2. **Extração de Texto**
```python
# Utiliza PyPDF2 para extrair texto dos PDFs
leitor = PyPDF2.PdfReader(file)
texto = "".join([pagina.extract_text() for pagina in leitor.pages])
```

### 3. **Processamento com CrewAI**
```python
def analise_feita_ia(curriculos_texto):
    crew = AnalisaPerfilECurriculo()
    inputs = {'curriculos': curriculos_texto}
    resultado = crew.crew().kickoff(inputs=inputs)
```

### 4. **Geração de Relatório**
```python
def cria_pdf(conteudo):
    # Gera PDF com timestamp único
    # Aplica limpeza de caracteres especiais
    # Formatação profissional
```

## 📊 Fluxo de Análise

### Processo Sequencial:
1. **Input**: Currículo em PDF
2. **Extração**: Conversão para texto
3. **RH Agent**: Análise cultural e técnica
4. **Comunicador Agent**: Formatação da resposta
5. **Output**: Relatório PDF estruturado

### Exemplo de Saída:
```
Candidato Pedro Vítor Batista Neres se assemelha aos valores culturais da ARMS por:

1. Inovação Tecnológica: Experiência comprovada em IA e APIs
2. Eficiência e Autonomia: Histórico de projetos independentes
3. Empoderamento: Foco em soluções estratégicas

Perfil identificado: Desenvolvedor Sênior com viés em Gestão
```

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install crewai PyPDF2 fpdf2 python-dotenv
```

### Configuração
1. Configure as variáveis de ambiente no arquivo `.env`
2. Certifique-se de ter as chaves de API necessárias

### Execução
```bash
python app.py
```

## 📈 Benefícios do Sistema

### **Para Recrutadores**
- Redução de 80% no tempo de triagem inicial
- Análises padronizadas e objetivas
- Foco em atividades estratégicas

### **Para Candidatos**
- Feedback estruturado e construtivo
- Transparência no processo seletivo
- Avaliação baseada em critérios claros

### **Para a Empresa**
- Maior alinhamento cultural nas contratações
- Processo escalável para grandes volumes
- Documentação automática das análises

## 🔧 Funcionalidades Técnicas

### **Processamento de Múltiplos Arquivos**
- Suporte a seleção em lote
- Consolidação de resultados em relatório único
- Tratamento de erros robusto

### **Limpeza de Texto**
```python
def limpar_texto(texto):
    # Remove caracteres especiais problemáticos
    # Normalização Unicode para compatibilidade PDF
    # Encoding otimizado para latin-1
```

### **Geração de PDF Profissional**
- Timestamp automático nos nomes de arquivo
- Formatação multi-linha inteligente
- Tratamento de caracteres especiais

## 📋 Configurações Avançadas

### **Customização de Agentes** (agents.yaml)
- Definição de roles e responsabilidades
- Configuração de experiência e backstory
- Ajuste de objetivos específicos

### **Personalização de Tarefas** (tasks.yaml)
- Instruções detalhadas para cada etapa
- Definição de outputs esperados
- Critérios de avaliação específicos

## 🎯 Casos de Uso

### **Recrutamento em Massa**
- Processos seletivos com centenas de candidatos
- Triagem inicial automatizada
- Pré-seleção baseada em critérios objetivos

### **Análise Cultural**
- Avaliação de fit cultural organizacional
- Identificação de perfis alinhados
- Feedback construtivo para desenvolvimento

### **Otimização de RH**
- Liberação de tempo para atividades estratégicas
- Padronização de processos seletivos
- Melhoria na qualidade das contratações

## 🔮 Perspectivas Futuras

- **Integração com ATS** (Applicant Tracking Systems)
- **Análise de soft skills** via processamento de linguagem natural
- **Dashboard web** para visualização de métricas
- **API REST** para integração com outros sistemas
- **Machine Learning** para melhoria contínua das análises

## 📞 Suporte e Contribuições

Este projeto demonstra a aplicação prática de IA multi-agente em processos de RH, combinando eficiência tecnológica com análise humana especializada para otimizar a seleção de talentos alinhados aos valores organizacionais.
