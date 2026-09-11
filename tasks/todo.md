# tasks/todo.md

## Sessão 2026-09-10/11 — Projeto de pesquisa: app de antibioticoterapia empírica (HEL + HCL)

Contexto: o usuário pediu a estrutura completa do projeto de pesquisa (justificativa, base de
conhecimento, passo a passo metodológico) para o app de antibioticoterapia empírica parametrizado
pela epidemiologia local de dois hospitais, com medida de conformidade antes-depois. Deliverable:
documentação em `docs/` + resumo no chat.

### ✅ FASE 1: Pesquisa e Protocolo Principal (CONCLUÍDA)

- [x] 1. Levantar referências verificáveis (2 subagentes: evidência clínica/AMS; métodos)
- [x] 2. Calcular tabela de tamanho amostral para cenários plausíveis de conformidade
- [x] 3. Escrever `docs/projeto_pesquisa_app_antibioticoterapia.md` com:
  - [x] identificação, resumo, introdução e justificativa
  - [x] hipóteses e objetivos
  - [x] base de conhecimento (6 tópicos da fundamentação teórica)
  - [x] método passo a passo (antibiograma → Delphi → app → usabilidade → conformidade)
  - [x] variáveis, desfechos, amostra, análise
  - [x] riscos, ética, LGPD, cronograma, orçamento, produtos, limitações
  - [x] 7 anexos técnicos (auditoria, Delphi, usabilidade, dados, amostra, regulatório, cronograma)
- [x] 4. Integrar 80 referências verificadas (63 PMID/DOI, 17 normativos)
- [x] 5. Revisar protocolo (consistência interna, nada inventado)
- [x] 6. Commit + push no branch `claude/antibiotic-prophylaxis-therapy-research-c3zya9`

**Status:** ✅ Concluído. Protocolo pronto: 655 linhas, 80 referências, 22 [DADO LOCAL], 15 [DECIDIR].

---

### ✅ FASE 2: Documentação de Coleta de Dados (CONCLUÍDA)

- [x] 1. Mapear 22 pontos [DADO LOCAL] do protocolo
- [x] 2. Estruturar coleta em 11 seções com tabelas de preenchimento
- [x] 3. Documentar 15 decisões [DECIDIR] com recomendações
- [x] 4. Criar checklist de preparação para CEP
- [x] 5. Compilar contatos e responsáveis por hospital
- [x] 6. Escrever `docs/coleta_dados_locais.md` (330 linhas)
- [x] 7. Commit + push

**Status:** ✅ Concluído. Formulário pronto para impressão e preenchimento com equipes locais.

---

### ✅ FASE 3: README e Visão Geral (CONCLUÍDA)

- [x] 1. Criar `docs/README_PESQUISA.md` como ponto de entrada
- [x] 2. Visualizar 5 etapas de pesquisa (antibiograma → compliance)
- [x] 3. Listar 15 decisões [DECIDIR] com status (✅/⏳/⚠️)
- [x] 4. Listar 22 dados locais [DADO LOCAL] por categoria e prioridade
- [x] 5. Descrever próximos passos (curto/médio/longo prazo)
- [x] 6. Referências regulatórias
- [x] 7. Commit + push

**Status:** ✅ Concluído. README pronto: 211 linhas.

---

## 📊 Documentação Entregue (1.196 linhas)

| Arquivo | Linhas | Propósito | Status |
|---------|--------|----------|--------|
| `projeto_pesquisa_app_antibioticoterapia.md` | 655 | Protocolo CEP-ready | ✅ |
| `coleta_dados_locais.md` | 330 | Formulário institucional | ✅ |
| `README_PESQUISA.md` | 211 | Visão geral e navegação | ✅ |
| **Total** | **1.196** | | **✅** |

---

## 🔄 FASE 4: Ação Local (AGUARDANDO USUÁRIO)

### Curto prazo (semanas 1-4)
- [ ] Preencher `coleta_dados_locais.md` com SCIH/farmácia/microbiologia/TI
- [ ] **CRÍTICO:** Resolver identificador de paciente no HCL (necessário para CLSI M39)
- [ ] Confirmar pesquisador responsável local em cada hospital
- [ ] Tomar decisões nos 15 pontos [DECIDIR]
- [ ] Compilar conformidade basal já medida (ou medir nos últimos 3-6 meses)

### Médio prazo (semanas 4-8)
- [ ] Levantar antibiogramas de 12 meses (HEL + HCL)
- [ ] Solicitar posicionamento formal à ANVISA sobre SaMD (RDC 657/2022)
- [ ] Revisar protocolo com SCIH/farmácia/microbiologia
- [ ] Inserir todos os dados locais no protocolo

### Longo prazo (semanas 8-12)
- [ ] Preparar TCLE (Termo de Consentimento Livre e Esclarecido)
- [ ] Agendar submissão ao CEP (Plataforma Brasil)
- [ ] Iniciar etapa 1: coleta e análise de antibiograma cumulativo

---

## ⚠️ Pontos Críticos Identificados

1. **HCL — Identificador de paciente:** A exportação atual do LIS traz apenas código de ordem de
   serviço, não ID de paciente. Necessário para aplicar a regra do "primeiro isolado" (CLSI M39).
   **Ação:** Contatar TI/Microbiologia antes de iniciar etapa 1.

2. **ANVISA SaMD:** O aplicativo (calculadora de dose + apoio à decisão) é enquadrável como
   software dispositivo médico (classe II, provável). Embora o projeto tenha atenuantes (uso interno,
   sem persistência de dados), a ANVISA recomenda posicionamento formal.
   **Ação:** Solicitar antes de implantar (seção 14 do protocolo).

3. **Contaminação entre hospitais:** Se >10% do corpo clínico atua em ambos, necessário escalonar
   implantação com 2-3 meses de intervalo. **Ação:** Estimar na seção 8 de `coleta_dados_locais.md`.

---

## 📝 Achados da Pesquisa

- **Nenhum MAUQ-BR:** Não existe validação em português do MAUQ; protocolo recomenda SUS-BR
  (Lourenço 2022) como instrumento principal.
- **Referências:** 80 fontes com 63 verificadas no PubMed (PMID/DOI); 17 normativos brasileiros
  (alguns gov.br/planalto bloqueados no ambiente, verificar antes de submeter ao CEP).
- **Ambiguidades do app:** 15 identificadas (A-01 a A-15) que serão resolvidas no painel Delphi.

---

## 🎯 Próximo Passo Recomendado

**Abrir [`docs/coleta_dados_locais.md`](../docs/coleta_dados_locais.md), imprimir e preencher com:**
1. SCIH (programa de AMS, estrutura, indicadores)
2. Farmácia (medicamentos restritos, auditoria, conformidade basal)
3. Microbiologia (LIS, exportação, antibiogramas, resistência)
4. TI (prescrição eletrônica, identificadores)
5. Administração (leitos, volumes, equipes)

---

## 📋 Comandos Git

Todos os commits estão no branch `claude/antibiotic-prophylaxis-therapy-research-c3zya9`:

```bash
git log --oneline claude/antibiotic-prophylaxis-therapy-research-c3zya9 -5
# d6a3c8a Adicionar README com visão geral do projeto de pesquisa
# 2e65ab8 Adicionar formulário de coleta de dados locais para protocolo de pesquisa
# [commits anteriores com protocolo principal]
```

---

**Última atualização:** 2026-09-11  
**Sessão:** session_019nvqa9tT3rvhK1RzTUc5Fw  
**Branch:** claude/antibiotic-prophylaxis-therapy-research-c3zya9
