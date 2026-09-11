# Projeto de Pesquisa: App de Antibioticoterapia Empírica

**Título:** Impacto de um Sistema de Apoio à Decisão para Antibioticoterapia Empírica na Conformidade com Protocolos Locais em Dois Hospitais de Londrina — Estudo Quase-Experimental com Série Temporal Interrompida

**Instituições:** Hospital Evangélico de Londrina (HEL) e Hospital do Câncer de Londrina (HCL)

**Status:** Em preparação para submissão ao CEP (Plataforma Brasil)

---

## Documentação

Este projeto de pesquisa é documentado em dois arquivos complementares:

### 1. **Protocolo de Pesquisa Completo**
📄 [`projeto_pesquisa_app_antibioticoterapia.md`](projeto_pesquisa_app_antibioticoterapia.md) — 655 linhas

**Conteúdo:**
- Identificação, resumo executivo, justificativa
- Hipóteses e objetivos
- Base de conhecimento (fundamentação teórica em 6 tópicos)
- Método em 5 etapas (antibiograma → Delphi → app → usabilidade → compliance)
- Variáveis, desfechos, amostra, análise estatística
- Riscos, ética, LGPD, cronograma, orçamento
- Produtos esperados e limitações
- 7 anexos técnicos (Anexos A–G)

**Referências:** 80 fontes verificadas (63 com PMID/DOI, 17 normativos)

**Marcadores especiais:**
- `[DADO LOCAL]` (22×): dados que só a instituição tem — leitos, volume, conformidade basal, estrutura laboratorial, resistência local
- `[DECIDIR]` (15×): decisões do pesquisador — com recomendações registradas

### 2. **Formulário de Coleta de Dados Locais**
📋 [`coleta_dados_locais.md`](coleta_dados_locais.md) — 330 linhas

**Conteúdo:**
- 11 seções estruturadas com tabelas de preenchimento
- Mapeamento 1:1 dos marcadores `[DADO LOCAL]` do protocolo
- Registro sistemático das 15 decisões do pesquisador
- Contatos e responsáveis por hospital
- Checklist de preparação para CEP

**Uso:** Imprima, preencha com SCIH/farmácia/microbiologia, use para completar o protocolo.

---

## Estrutura das 5 Etapas de Pesquisa

```
ETAPA 1: ANTIBIOGRAMA CUMULATIVO
├─ Período: 12 meses retroativos
├─ Método: CLSI M39 + pontos BrCAST
├─ Saída: Matriz de prevalência de resistência por hospital
└─ Responsável: Microbiologia

ETAPA 2: VALIDAÇÃO DELPHI
├─ Painel: 12-18 especialistas/hospital
├─ Rodadas: Até convergência (máx. 4)
├─ Saída: Recomendações empíricas validadas
└─ Responsável: SCIH/Farmácia + investigador

ETAPA 3: PARAMETRIZAÇÃO DO APP
├─ Tecnologia: TypeScript/React (aplicativo web progressivo)
├─ Testes: 59 testes de fidelidade ao protocolo
├─ Saída: Aplicativo pronto para implantação
└─ Responsável: Desenvolvedor

ETAPA 4: TESTE DE USABILIDADE
├─ Instrumento: SUS-BR + MAUQ (formulários prescrição)
├─ Amostra: ≥30 prescritores por hospital
├─ Saída: Relatório de usabilidade somativa
└─ Responsável: Farmácia + investigador

ETAPA 5: AUDITORIA DE CONFORMIDADE
├─ Desenho: Série temporal interrompida
├─ Período: 12 meses antes + 12 meses depois
├─ Análise: Regressão logística + regressão segmentada
├─ Desfecho primário: Proporção de prescrições empíricas globalmente conformes
└─ Responsável: Estatístico + auditoria
```

---

## Decisões Pendentes (15 pontos [DECIDIR])

| # | Decisão | Seção | Status | Recomendação |
|---|---------|-------|--------|--------------|
| 1 | Simultaneidade vs. escalonamento de implantação | 6 | ⏳ | Escalonar 2-3 meses se contaminação >10% |
| 2 | Duração da coleta pós-implantação | 6 | ⏳ | 12 meses |
| 3 | Tamanho do painel Delphi | 6 | ⏳ | 12-18 especialistas/hospital |
| 4 | Rodadas Delphi necessárias | 6 | ⏳ | Até convergência, máx. 4 |
| 5 | Linguagem/tecnologia do app | 6 | ✅ | TypeScript/React (mantém off-line) |
| 6 | Telemetria de uso | 7 | ⏳ | Apenas endereço curto agregado (privacidade) |
| 7 | Desfecho primário | 8 | ⏳ | Conformidade global estrita (vs. adequação) |
| 8 | Desfecho de controle não-equivalente | 8 | ⏳ | Medir profilaxia cirúrgica se timeline não sobrepõe |
| 9 | Amostragem de prescrições | 8 | ⏳ | Todos se <150/mês; senão amostra aleatória |
| 10 | Posicionamento ANVISA sobre SaMD | 14 | ⚠️ | Solicitar formalmente antes de implantar |
| 11 | Persistir dados de paciente no app? | 7 | ✅ | Não (simplifica LGPD) |
| 12 | Identificador de paciente no LIS | 5 | ⚠️ | HCL: resolver com TI/Microbiologia |
| 13 | Profissionais compartilhados | 6 | ⏳ | Estimar % e definir estratégia de comunicação |
| 14 | Duração da coleta pré-implantação | 7 | ⏳ | Conforme volume (vide tabela amostral) |
| 15 | Equipe central de desenvolvedores | 12 | ⏳ | Confirmar estatístico e desenvolvedor |

**Legenda:** ✅ = Resolvido | ⏳ = Aguardando informação local | ⚠️ = Requer ação externa

---

## Dados Locais Necessários (22 pontos [DADO LOCAL])

| Categoria | Hospitais | Seções | Prioridade |
|-----------|-----------|--------|-----------|
| **Estrutura** | HEL, HCL | 1, 5 | Alta |
| **SCIH/AMS** | HEL, HCL | 5 | Alta |
| **LIS/Microbiologia** | HEL, HCL | 5 | **Crítica** |
| **Conformidade basal** | HEL, HCL | 5 | Alta |
| **Resistência** | HEL, HCL | 5 | Alta |
| **Corpo clínico** | HEL, HCL | 5 | Média |
| **Volumes prescrições** | HEL, HCL | 7-8 | Alta |
| **Contaminação** | HEL, HCL | 6 | Média |
| **Equipes/contatos** | HEL, HCL | 12 | Alta |

**Ação:** Use [`coleta_dados_locais.md`](coleta_dados_locais.md) para coleta sistemática.

---

## Anexos Técnicos

No arquivo principal, incluídos 7 anexos:

| Anexo | Título | Linhas |
|-------|--------|--------|
| **Anexo A** | Instrumento de auditoria de conformidade | 30 |
| **Anexo B** | Roteiro Delphi (exemplo de rodada 1) | 15 |
| **Anexo C** | Itens de usabilidade: SUS-BR + MAUQ | 20 |
| **Anexo D** | Estrutura de dados de antibiograma (CLSI M39) | 12 |
| **Anexo E** | Tabela de tamanho amostral | 20 |
| **Anexo F** | Despacho Inaep nº 3/2026 (resumo) | 8 |
| **Anexo G** | Cronograma sugerido (18 meses) | 12 |

---

## Próximos Passos

### Curto prazo (semanas 1-4)
- [ ] Preencher `coleta_dados_locais.md` com SCIH/farmácia/microbiologia
- [ ] Resolver identificador de paciente do HCL (crítico para antibiograma)
- [ ] Confirmar pesquisador responsável local em cada hospital
- [ ] Tomar decisões nos 15 pontos [DECIDIR]

### Médio prazo (semanas 4-8)
- [ ] Compilar conformidade basal medida em cada hospital
- [ ] Levantar antibiogramas de 12 meses
- [ ] Solicitar posicionamento formal à ANVISA (SaMD)
- [ ] Revisar protocolo com SCIH/farmácia/microbiologia

### Longo prazo (semanas 8-12)
- [ ] Inserir dados locais no protocolo
- [ ] Preparar TCLE (Termo de Consentimento)
- [ ] Agendar submissão ao CEP (Plataforma Brasil)
- [ ] Iniciar etapa 1: antibiograma cumulativo

---

## Contatos e Responsabilidades

Use a seção 10 de [`coleta_dados_locais.md`](coleta_dados_locais.md) para registrar:
- Pesquisadores responsáveis locais (HEL, HCL)
- Farmacêuticos clínicos
- Microbiologistas
- Representantes SCIH
- Campeões por unidade
- Equipe central (estatístico, desenvolvedor, coordenador)

---

## Referências e Regulação

- **80 referências** verificadas no protocolo (PMID/DOI/regulatórias)
- **Lei 14.874/2024** — Regulamento de Pesquisa Clínica
- **Decreto 12.651/2025** — Regulamentação de CEP/CONEP
- **Despacho Inaep nº 3/2026** — Multicêntrica com CEP único
- **RDC 657/2022 + RDC 751/2022** (ANVISA) — Software como dispositivo médico (SaMD)
- **LGPD** — Lei Geral de Proteção de Dados

**Nota:** Alguns documentos de gov.br/planalto não puderam ser acessados no ambiente de desenvolvimento; verificar links antes de submeter ao CEP.

---

## Tecnologia do Aplicativo

- **Repositório:** `src/components/AntibioticGuide/` (TypeScript/React)
- **Funcionalidades:** 16 cards de orientação, 6 tabelas de protocolo, calculadora de dose por peso, modo alergia, funcionamento offline
- **Testes:** 59 testes automatizados verificam fidelidade ao protocolo
- **Ambiguidades identificadas:** 15 (A-01 a A-15) a resolver via Delphi

---

## Versão do Protocolo

- **Data de criação:** 2026-09-10
- **Última atualização:** 2026-09-11
- **Branch Git:** `claude/antibiotic-prophylaxis-therapy-research-c3zya9`
- **Arquivos:**
  - `docs/projeto_pesquisa_app_antibioticoterapia.md` (protocolo principal)
  - `docs/coleta_dados_locais.md` (formulário de coleta)
  - `docs/README_PESQUISA.md` (este arquivo)

---

**Para começar:** Abra [`coleta_dados_locais.md`](coleta_dados_locais.md), imprima, e preencha com sua equipe.
