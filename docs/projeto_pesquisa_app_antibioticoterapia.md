# Projeto de pesquisa — Aplicativo de apoio à decisão para antibioticoterapia empírica parametrizado pela epidemiologia local

**Subtítulo:** validação por consenso e efeito sobre a conformidade das prescrições em dois hospitais de Londrina, PR (Hospital Evangélico de Londrina e Hospital do Câncer de Londrina)

Versão 0.1, rascunho estrutural, 10/09/2026. Pesquisador responsável: Dr. Philipe Bellinati, Coordenador do SCIH do Hospital Evangélico de Londrina.

---

## Como usar este documento

- A ordem das seções segue o "Projeto Detalhado" exigido na Plataforma Brasil e os campos do formulário eletrônico (resumo, introdução, hipótese, objetivos, metodologia, critérios de inclusão e exclusão, riscos e benefícios, desfechos, cronograma, orçamento).
- `[DADO LOCAL]` marca número ou fato que só a instituição tem (leitos, volume de prescrições, conformidade basal). `[DECIDIR]` marca uma decisão do pesquisador responsável, sempre com a recomendação registrada ao lado. `[REF n]` aponta para o item n da lista de referências da seção 20.
- Nenhum número deste documento foi inventado. Onde não há dado verificado, há marcador.
- As seções 6 (base de conhecimento) e 7 (método passo a passo) são o núcleo pedido: o que escrever na fundamentação teórica e como executar cada etapa.

---

## 1. Identificação

| Campo | Conteúdo |
|---|---|
| Título | Aplicativo de apoio à decisão para antibioticoterapia empírica parametrizado pela epidemiologia local: validação por consenso e efeito sobre a conformidade das prescrições em dois hospitais de Londrina |
| Título curto | App-ATB Londrina |
| Desenho | Estudo multicêntrico, misto, em fases: metodológico (desenvolvimento e validação) seguido de quase-experimental antes-depois com série temporal interrompida |
| Instituição proponente e centro coordenador | Hospital Evangélico de Londrina (AEBEL) |
| Centro participante | Hospital do Câncer de Londrina (ICL) `[DADO LOCAL: razão social e pesquisador responsável local]` |
| Área temática (Plataforma Brasil) | Não se enquadra em área temática especial; grande área Ciências da Saúde; Medicina / Infectologia |
| Palavras-chave | Gestão de antimicrobianos; sistemas de apoio a decisões clínicas; aplicativos móveis; fidelidade a diretrizes; técnica Delphi; estudos quase-experimentais |
| Financiamento | Próprio / institucional `[DECIDIR]` |
| Registro | ReBEC (registrar antes do início da coleta prospectiva) |

---

## 2. Resumo estruturado (rascunho)

**Introdução.** A prescrição empírica de antimicrobianos concentra a maior parte do uso hospitalar e a maior parte da inadequação. Protocolos institucionais em papel têm adesão limitada por barreiras de acesso, atualização e complexidade. Aplicativos móveis que entregam o protocolo no ponto de prescrição são intervenção de baixo custo com evidência de aumento de adesão, mas há poucos estudos brasileiros, quase todos unicêntricos, sem parametrização formal pela epidemiologia local e sem medida padronizada de conformidade.

**Objetivo.** Desenvolver, validar e implantar instâncias de um aplicativo de apoio à decisão para antibioticoterapia empírica, cada uma parametrizada pelo perfil de sensibilidade e pelo protocolo do respectivo hospital, e estimar o efeito da implantação sobre a conformidade das prescrições empíricas com o protocolo institucional.

**Método.** Estudo multicêntrico em dois hospitais de Londrina (um geral e um oncológico), em cinco etapas: (1) antibiograma cumulativo de 12 meses por hospital, segundo CLSI M39 e pontos de corte BrCAST; (2) elaboração da matriz de recomendações empíricas por foco, população e setor e validação por técnica Delphi com painel de especialistas de cada hospital; (3) parametrização do aplicativo com o conteúdo validado, verificação automatizada da fidelidade ao protocolo e teste formativo de usabilidade; (4) implantação com pacote de divulgação e avaliação somativa de usabilidade (SUS e MAUQ) entre prescritores; (5) auditoria da conformidade das prescrições empíricas em `[DADO LOCAL]` meses antes e 12 meses depois da implantação, com o mesmo instrumento, analisada por regressão logística e por regressão segmentada de série temporal interrompida. Desfecho primário: proporção de prescrições empíricas globalmente conformes ao protocolo institucional.

**Resultados esperados.** Duas instâncias validadas do aplicativo, um protocolo de antibioticoterapia empírica para o hospital oncológico derivado da epidemiologia local, medidas de usabilidade e a estimativa do efeito da implantação sobre a conformidade em cada hospital e no conjunto.

---

## 3. Introdução e justificativa: roteiro argumentativo

Escreva a introdução como um funil de sete parágrafos. Cada item abaixo diz o que o parágrafo precisa afirmar e o que precisa citar.

1. **Magnitude do problema.** Resistência antimicrobiana como causa direta de mortes no mundo (estimativa GRAM 2019, Murray et al. 2022) e as infecções relacionadas à assistência à saúde como principal cenário hospitalar. No Brasil, alta prevalência de enterobactérias produtoras de carbapenemase e de *Acinetobacter* resistente a carbapenêmicos nos boletins da ANVISA `[REF 1-3]`. Em pacientes oncológicos, a neutropenia febril e a colonização por bacilos gram-negativos multirresistentes elevam o risco `[REF 30, 33, 35, 36]`.
2. **Uso empírico como alvo.** A maior parte das prescrições hospitalares começa empírica, e é nessa janela que se decidem espectro, dose e duração. Estudos de prevalência pontual e auditorias mostram proporção substancial de esquemas empíricos inadequados `[REF 21-26]`. Inserir aqui a conformidade basal já medida nos dois hospitais `[DADO LOCAL]`: é o argumento mais forte da justificativa, porque prova que o problema existe localmente e que é mensurável.
3. **Política pública.** O gerenciamento do uso de antimicrobianos é exigido pela Diretriz Nacional da ANVISA e é meta do PNPCIRAS 2021-2025; a Portaria MS 2.616/1998 atribui à CCIH a normatização do uso racional de antimicrobianos; a OMS propõe a classificação AWaRe como métrica de qualidade `[REF 2-9]`. Protocolos institucionais baseados em epidemiologia local são o componente central desses programas.
4. **Por que o protocolo em papel não basta.** Barreiras conhecidas: acesso no momento da prescrição, desatualização, extensão do documento, hierarquia e "etiqueta de prescrição", carga cognitiva em plantão `[REF 27, 28]`. Disponibilizar a diretriz não garante adesão; a mudança de comportamento exige capacidade, oportunidade e motivação (modelo COM-B) `[REF 29]`.
5. **A solução proposta e sua evidência.** Aplicativos móveis e sistemas de apoio à decisão que entregam o protocolo no ponto de prescrição aumentam a adesão e reduzem uso de amplo espectro em revisões sistemáticas `[REF 13-16]`, e dois ensaios randomizados escalonados recentes, um multicêntrico europeu e um em hospitais do Laos, confirmaram efeito sobre a adequação da terapia empírica com aplicativos que entregam diretrizes locais `[REF 17, 18]`. Uma série temporal mostrou adesão sustentada ao longo de anos `[REF 20]`. No Brasil há um estudo unicêntrico em Curitiba `[REF 12]` e uma metanálise nacional recente sobre eHealth e terapia empírica adequada `[REF 19]`.
6. **Lacuna e originalidade.** Faltam estudos brasileiros que (a) derivem o conteúdo do aplicativo formalmente do antibiograma cumulativo local, (b) validem o conteúdo por consenso estruturado, (c) usem um mesmo motor de decisão instanciado em hospitais com epidemiologias distintas, o que testa transferibilidade, e (d) meçam conformidade com instrumento padronizado antes e depois, com série temporal. Este projeto faz as quatro coisas em um hospital geral e em um hospital oncológico, onde a neutropenia febril e a resistência a carbapenêmicos exigem conteúdo próprio `[REF 30-36]`.
7. **Justificativa institucional e viabilidade.** O Hospital Evangélico já possui protocolo revisado em março de 2026 e uma instância funcional do aplicativo, construída sob o princípio "o protocolo é dado, não código", com testes automatizados que provam a fidelidade de cada célula do protocolo. O Hospital do Câncer possui base de dados de sensibilidade e painel analítico próprio. Os dois serviços já auditam conformidade `[DADO LOCAL: desde quando, com que instrumento]`. O custo marginal da intervenção é baixo e o resultado é transferível a outros hospitais.

Feche a introdução com a pergunta de pesquisa: *Em dois hospitais com epidemiologias distintas, a implantação de um aplicativo de antibioticoterapia empírica parametrizado pela epidemiologia local e validado por consenso aumenta a conformidade das prescrições empíricas com o protocolo institucional em comparação com o período anterior, em que o protocolo estava disponível apenas em papel?*

---

## 4. Hipóteses

- **H1 (primária).** Após a implantação do aplicativo, a proporção de prescrições empíricas globalmente conformes ao protocolo institucional é maior do que no período anterior, em cada hospital.
- **H2.** O efeito ocorre como mudança de nível na série temporal mensal imediatamente após a implantação e se mantém ao longo de 12 meses (sem decaimento significativo da inclinação).
- **H3.** A conformidade melhora nos componentes que o aplicativo apoia diretamente (escolha do antimicrobiano, dose, via, intervalo, ajuste por peso e por função renal) mais do que nos componentes que ele não apoia diretamente (coleta de culturas antes da primeira dose, reavaliação documentada em 48 a 72 h).
- **H4.** A usabilidade percebida pelos prescritores é aceitável nos dois hospitais (escore SUS médio igual ou superior a 70, na versão brasileira da escala).
- **H5 (exploratória).** O efeito é semelhante entre os hospitais, o que sustenta a transferibilidade do motor de decisão parametrizado.

---

## 5. Objetivos

### 5.1 Objetivo geral

Desenvolver, validar e implantar um aplicativo de apoio à decisão para antibioticoterapia empírica parametrizado pela epidemiologia de cada hospital e estimar o efeito de sua implantação sobre a conformidade das prescrições empíricas com o protocolo institucional no Hospital Evangélico de Londrina e no Hospital do Câncer de Londrina.

### 5.2 Objetivos específicos (cada um corresponde a uma etapa do método)

1. Descrever o perfil de sensibilidade de cada hospital por meio de antibiograma cumulativo de 12 meses, estratificado por setor e material, e derivar dele as opções empíricas por foco infeccioso, população e setor.
2. Elaborar a matriz de recomendações empíricas de cada hospital e validar seu conteúdo por técnica Delphi com painel de especialistas locais, incluindo a resolução das ambiguidades identificadas na transcrição do protocolo vigente.
3. Parametrizar uma instância do aplicativo para cada hospital com o conteúdo validado, verificar a fidelidade do aplicativo ao protocolo por testes automatizados e por conferência independente, e corrigir problemas de usabilidade em teste formativo.
4. Implantar o aplicativo com um pacote de divulgação padronizado e avaliar a usabilidade, a aceitação e o alcance entre os prescritores.
5. Medir a conformidade das prescrições empíricas com o protocolo institucional antes e depois da implantação, com o mesmo instrumento, e estimar o efeito da implantação em cada hospital e no conjunto, por regressão logística e por série temporal interrompida.
6. Descrever a implantação (alcance, adoção, manutenção) e as barreiras e facilitadores percebidos, para orientar a transferência a outros hospitais.

---

## 6. Base de conhecimento: o que a fundamentação teórica precisa cobrir

Cada tópico traz o que dizer, o argumento que ele sustenta no projeto, as referências-chave e o dado local a inserir. A lista numerada de referências, com PMID e DOI, está na seção 20.

### 6.1 Resistência antimicrobiana e infecções relacionadas à assistência à saúde

- **O que cobrir.** Carga global de mortes atribuíveis e associadas à resistência; principais patógenos; situação brasileira (boletins ANVISA de IRAS e resistência; BR-GLASS); particularidades do paciente oncológico (neutropenia, mucosite, cateteres, colonização por multirresistentes, mortalidade da bacteremia por gram-negativo resistente).
- **Argumento.** Dimensiona o problema e justifica que o alvo seja a prescrição empírica hospitalar em dois perfis distintos de paciente.
- **Referências-chave.** Murray et al. 2022 (GRAM); ANVISA, boletins de segurança do paciente e qualidade em serviços de saúde; Schonardie et al. 2023 e de Souza et al. 2024 sobre resistência em pacientes onco-hematológicos brasileiros `[REF 1, 35, 36]`.
- **Dado local.** Prevalência dos principais fenótipos de resistência em cada hospital no ano anterior, extraída do antibiograma cumulativo (seção 7, etapa 1) `[DADO LOCAL]`.

### 6.2 Gerenciamento do uso de antimicrobianos (antimicrobial stewardship)

- **O que cobrir.** Definição, elementos essenciais (liderança, responsabilidade, expertise farmacêutica, ações, monitoramento, relato, educação), tipos de intervenção (persuasivas, restritivas, estruturais), evidência de efetividade (Cochrane 2017: aumento de adesão a políticas e redução de permanência sem aumento de mortalidade), marco brasileiro (Diretriz Nacional ANVISA; PNPCIRAS; Portaria 2.616/1998), métricas (DOT, DDD, AWaRe).
- **Argumento.** Posiciona o aplicativo como intervenção estrutural e persuasiva dentro de um programa de gerenciamento já existente nos dois hospitais, e não como ação isolada.
- **Referências-chave.** Barlam et al. 2016 (IDSA/SHEA); Davey et al. 2017 (Cochrane); CDC Core Elements 2019; OMS AWaRe 2023 e Moja et al. 2024; ANVISA Diretriz Nacional (2017, revisada em 2023); PNPCIRAS vigente na data da submissão; Portaria MS 2.616/1998 `[REF 2-9]`.
- **Dado local.** Estrutura do programa em cada hospital: equipe, reuniões, restrição de antimicrobianos, auditoria prospectiva com feedback, indicadores acompanhados `[DADO LOCAL]`.

### 6.3 Terapia empírica guiada pela epidemiologia local

- **O que cobrir.** Antibiograma cumulativo: método CLSI M39 (primeiro isolado por paciente por período, mínimo de 30 isolados por espécie, exclusão de triagens de vigilância, estratificação por setor e material), pontos de corte BrCAST, limitações (viés de coleta, isolados de colonização, agregação de unidades), antibiogramas sindrômicos e combinados, e a tradução do antibiograma em recomendação (probabilidade de cobertura desejada por gravidade do quadro, por exemplo, mais alta em sepse e neutropenia febril do que em infecção urinária não complicada).
- **Argumento.** Fundamenta a etapa 1 e explica por que o conteúdo do aplicativo precisa ser diferente em cada hospital.
- **Referências-chave.** CLSI M39, 5ª edição; Hindler & Stelling 2007; BrCAST; Hebert et al. 2012 (antibiograma sindrômico ponderado, WISCA); Averbuch et al. 2013 (ECIL-4, escalonamento guiado pela epidemiologia local) `[REF 33, 37-40]`.
- **Dado local.** Sistema de informação laboratorial de cada hospital, campos disponíveis na exportação e existência de identificador de paciente (necessário para a regra do primeiro isolado; a exportação atual do HCL traz código de ordem de serviço, não identificador de paciente; ver Anexo D) `[DADO LOCAL]`.

### 6.4 Conformidade e adequação da prescrição: conceitos e medida

- **O que cobrir.** Distinção entre *adesão* ao protocolo (critério objetivo, reprodutível) e *adequação* clínica (juízo de especialista, admite desvios justificados); componentes da prescrição avaliáveis (indicação, escolha, dose, via, intervalo, duração, coleta de culturas, tempo até a primeira dose, reavaliação, descalonamento); métodos de medida (auditoria de prontuário, prevalência pontual como Global-PPS e ECDC-PPS, indicadores de consumo); confiabilidade entre avaliadores; o problema da "caixa preta" da adequação (Spivak 2016).
- **Argumento.** Justifica o desfecho primário, o instrumento do Anexo A e a exigência de dois avaliadores com kappa.
- **Referências-chave.** Spivak, Cosgrove & Srinivasan 2016; DePestel et al. 2014; Versporten et al. 2018 (Global-PPS); Porto et al. 2020 (Global-PPS em hospitais brasileiros); Cambiais et al. 2026 (auditoria por "quatro momentos" no HC-FMUSP); Raniero et al. 2025 (adesão a protocolo de neutropenia febril em hospital oncológico brasileiro) `[REF 21-26]`.
- **Dado local.** Instrumento e resultados da conformidade já medida nos dois hospitais, por componente, com o período e o número de prescrições auditadas `[DADO LOCAL]`.

### 6.5 Determinantes comportamentais da prescrição e mudança de comportamento

- **O que cobrir.** "Etiqueta de prescrição" e autonomia clínica, hierarquia, medo de errar por omissão, incerteza diagnóstica, influência dos pares; modelo COM-B e Roda de Mudança de Comportamento; por que ferramentas no ponto de decisão atuam sobre *capacidade* (conhecimento acessível) e *oportunidade* (tempo, ambiente), mas dependem de *motivação* e de endosso institucional.
- **Argumento.** Explica o mecanismo pelo qual o aplicativo deve funcionar e justifica o pacote de divulgação e os "campeões" locais na etapa 4.
- **Referências-chave.** Charani et al. 2013 (Clin Infect Dis); Hulscher et al. 2010; Michie, van Stralen & West 2011 `[REF 27-29]`.
- **Dado local.** Composição do corpo clínico (proporção de residentes, plantonistas, rotatividade) e resultados de pesquisas de percepção anteriores, se existirem `[DADO LOCAL]`.

### 6.6 Sistemas de apoio à decisão clínica e aplicativos móveis em antimicrobianos

- **O que cobrir.** Taxonomia (integrados ao prontuário eletrônico versus autônomos; guia de referência versus recomendação individualizada); "cinco certos" do apoio à decisão (informação certa, para a pessoa certa, no formato certo, pelo canal certo, no momento certo); evidência de revisões sistemáticas e de estudos primários com aplicativos de política de antimicrobianos; experiência brasileira; riscos (erro de conteúdo, falsa segurança, desatualização) e salvaguardas (fidelidade ao documento controlado, controle de versão, responsabilidade do prescritor).
- **Argumento.** Sustenta a escolha de um guia autônomo, off-line, sem dado de paciente, com conteúdo derivado de documento controlado, e antecipa as perguntas do CEP sobre risco.
- **Referências-chave.** Baysari et al. 2016; Curtis et al. 2017; Helou et al. 2020; Rittmann & Stevens 2019; Charani et al. 2013 (JAC); Panesar et al. 2016; Tuon et al. 2017; Helou et al. 2025 (ensaio escalonado multicêntrico); Chansamouth et al. 2026 (ensaio escalonado no Laos); Tuon et al. 2024 (metanálise brasileira); Yoon et al. 2023 (série temporal) `[REF 10-20]`.
- **Dado local.** Descrição da instância já existente no Hospital Evangélico: 16 fichas, seis tabelas do protocolo (6.1 a 6.6), calculadora de dose por peso, ajuste renal, modo alergia, cronômetro de janelas, funcionamento off-line, ausência de telemetria, 59 testes automatizados, e as 15 ambiguidades do protocolo documentadas (A-01 a A-15) que a etapa 2 vai resolver.

### 6.7 Desenvolvimento e validação de tecnologias em saúde

- **O que cobrir.** Ciclo de desenvolvimento centrado no usuário; validação de conteúdo (Delphi, índice de validade de conteúdo, método RAND/UCLA de adequação) e diretriz de relato ACCORD; validação técnica (testes automatizados de regras clínicas, verificação de fidelidade célula a célula); usabilidade segundo ISO 9241-11 (eficácia, eficiência, satisfação), instrumentos SUS e MAUQ em versão brasileira, teste formativo com poucos usuários e teste somativo com amostra maior; diretriz mERA para relato de intervenções mHealth.
- **Argumento.** Fundamenta as etapas 2, 3 e 4 e define os critérios de sucesso de cada uma.
- **Referências-chave.** Diamond et al. 2014; Nasa et al. 2021; Jünger et al. 2017 (CREDES); Gattrell et al. 2024 (ACCORD); Fitch et al. 2001 (RAND/UCLA); Rocha et al. 2025 e Nucci et al. 2024 (precedentes brasileiros de Delphi para aplicativo e para protocolo de neutropenia febril); Polit & Beck 2006; Lynn 1986; Alexandre & Coluci 2011; Brooke 1996; Lewis 2018; Lourenço et al. 2022 (SUS em português do Brasil); Zhou et al. 2019 (MAUQ, sem versão brasileira localizada); Stoyanov et al. 2016 (uMARS); Nielsen & Landauer 1993; ISO 9241-11; Agarwal et al. 2016 (mERA) `[REF 41-57, 67]`.
- **Dado local.** Nenhum além da equipe disponível para o painel Delphi.

### 6.8 Desenhos quase-experimentais para avaliar intervenções em antimicrobianos

- **O que cobrir.** Limites do antes-depois simples (tendência secular, sazonalidade, regressão à média, efeito Hawthorne, cointervenções); série temporal interrompida com regressão segmentada (mudança de nível e de inclinação, autocorrelação, número mínimo de pontos por segmento); desenho escalonado entre centros; desfechos de controle não equivalentes; recomendações de consenso para desenho de estudos de stewardship; diretrizes de relato TREND e SQUIRE 2.0; TIDieR para descrever a intervenção; StaRI para relatar a implantação.
- **Argumento.** Justifica o desenho da etapa 5, a análise por série temporal e as análises de sensibilidade.
- **Referências-chave.** Bernal, Cummins & Gasparrini 2017; Wagner et al. 2002; Penfold & Zhang 2013; Harris et al. 2004; Shardell et al. 2007; Schweitzer et al. 2020; Hemming et al. 2015; Des Jarlais et al. 2004 (TREND); Ogrinc et al. 2016 (SQUIRE 2.0); Hoffmann et al. 2014 (TIDieR); Pinnock et al. 2017 (StaRI) `[REF 58-69]`.
- **Dado local.** Volume mensal de prescrições empíricas elegíveis em cada hospital, para dimensionar os pontos da série `[DADO LOCAL]`.

### 6.9 Ciência da implementação

- **O que cobrir.** Desfechos de implementação (aceitabilidade, adoção, adequação, viabilidade, fidelidade, alcance, sustentabilidade); estrutura RE-AIM; domínios do CFIR para descrever contexto, barreiras e facilitadores.
- **Argumento.** Dá vocabulário ao objetivo 6 e ao relato da etapa 4.
- **Referências-chave.** Proctor et al. 2011; Glasgow, Vogt & Boles 1999; Damschroder et al. 2009 e 2022 `[REF 70-73]`.

### 6.10 Aspectos éticos, legais e regulatórios

- **O que cobrir.** Lei 14.874/2024 e Decreto 12.651/2025 (análise ética única em estudo multicêntrico, prazos); Resoluções CNS 466/2012 e 674/2022 no que não conflitam; dispensa justificada de TCLE para auditoria de prescrições; TCLE de profissionais nas etapas Delphi e usabilidade; LGPD (bases legais para pesquisa, pseudonimização, cada hospital como controlador); ANVISA RDC 657/2022 e RDC 751/2022: o documento de perguntas e respostas da ANVISA enquadra como software dispositivo médico a calculadora de dose e o sistema de apoio à decisão que sugere medicação a partir de protocolo publicado, o que atinge este aplicativo e exige análise de enquadramento documentada (seção 13); resoluções do CFM sobre documentos eletrônicos e telemedicina, para deixar claro que o aplicativo não emite prescrição; conflito de interesse do pesquisador que é autor do protocolo e coordenador do SCIH.
- **Argumento.** Antecipa as pendências mais prováveis do CEP e o risco regulatório.
- **Referências-chave.** Textos legais e normativos `[REF 74-80]`.

### 6.11 Contexto local

- **O que cobrir.** Cada hospital: natureza, porte, leitos por tipo (enfermaria adulto e pediátrica, UTI adulto, pediátrica e neonatal, unidade coronariana e neurológica no Evangélico; unidades oncológicas, hematologia, UTI e pronto atendimento no Hospital do Câncer), volume anual de internações e de prescrições de antimicrobianos, estrutura do SCIH e da farmácia clínica, sistema de prescrição (eletrônica ou papel), laboratório de microbiologia e sistema de informação `[DADO LOCAL]`.
- **Argumento.** Permite ao leitor e ao CEP julgar viabilidade e generalização, e é exigido pelas diretrizes de relato.

---

## 7. Método passo a passo

### 7.0 Desenho geral

Estudo multicêntrico em duas fases. A fase metodológica (etapas 1 a 3) produz e valida a intervenção. A fase avaliativa (etapas 4 e 5) mede usabilidade e efeito por desenho quase-experimental antes-depois com série temporal interrompida, em cada hospital, com análise conjunta. A implantação pode ser simultânea ou escalonada entre os hospitais `[DECIDIR]`; a recomendação é escalonar em dois a três meses, porque o hospital que ainda não implantou funciona como controle concorrente do outro no intervalo, e porque a equipe de implantação se concentra em um hospital por vez. Atenção ao risco de contaminação: parte dos prescritores atua nos dois hospitais `[DADO LOCAL: estimar a proporção]`; a instância de cada hospital deve ser visualmente distinta e o acesso divulgado só no hospital correspondente.

### Etapa 0. Harmonizar a linha de base já existente

Os dois serviços já medem conformidade com o protocolo em papel. Antes de qualquer outra coisa:

1. Recuperar o instrumento usado, o período coberto, os critérios de inclusão, quem auditou e quantas prescrições foram avaliadas por mês `[DADO LOCAL]`.
2. Comparar esse instrumento com o do Anexo A. Se os componentes e as regras de julgamento forem os mesmos, a linha de base é usada como está. Se diferirem, reauditar uma amostra aleatória do período basal com o instrumento do estudo (ao menos 30 prescrições por mês, ou todas se houver menos) e reportar a concordância. O que não pode acontecer é comparar períodos medidos com réguas diferentes.
3. Definir a janela pré-intervenção: 12 meses imediatamente anteriores à implantação é o ideal para a série temporal; o mínimo aceitável é 8 pontos mensais.
4. Registrar cointervenções ocorridas no período basal (mudança de protocolo, entrada de farmacêutico clínico, campanhas), porque entram como covariáveis ou como cortes na série.

### Etapa 1. Perfil de sensibilidade de cada hospital

**Fonte.** Exportação do sistema do laboratório de microbiologia dos 12 meses anteriores ao início do estudo. A exportação já usada no painel do Hospital do Câncer traz código da ordem de serviço, data, unidade de coleta, material, microrganismo, antimicrobiano e classificação; falta um identificador pseudonimizado de paciente, que é obrigatório para aplicar a regra do primeiro isolado `[DADO LOCAL: solicitar campo ao laboratório]`.

**Regras de processamento (CLSI M39).**

- Um isolado por paciente, por espécie, por período de análise (primeiro isolado), independentemente do material e do setor; variante aceitável: primeiro isolado por paciente, por espécie, por setor, quando o antibiograma for estratificado por setor.
- Excluir culturas de vigilância (swabs de triagem) e resultados negativos.
- Reportar apenas espécies com 30 ou mais isolados no período; abaixo disso, agrupar (por exemplo, "complexo *Enterobacter cloacae* e outras enterobactérias") ou marcar como estimativa imprecisa.
- Reportar percentual de sensíveis, com o número de isolados testados por droga; não reportar drogas testadas em menos de 30 isolados sem essa ressalva.
- Interpretar pelos pontos de corte BrCAST vigentes; registrar a versão.
- Estratificar por setor (UTI adulto, UTI pediátrica e neonatal, enfermarias, pronto atendimento, unidades oncológicas) e por material (sangue, urina, trato respiratório, sítio cirúrgico, outros).
- Tratar separadamente o resultado de polimixina B extraído das observações do isolado, como já faz o processador do painel.

**Produtos.**

1. Tabelas de antibiograma cumulativo por hospital, por setor e por material, com a data de geração e a versão dos pontos de corte.
2. Antibiogramas sindrômicos para os focos do protocolo (pneumonia hospitalar, infecção urinária associada a cateter, corrente sanguínea, neutropenia febril no hospital oncológico), com a probabilidade estimada de cobertura de cada esquema candidato.
3. Uma nota metodológica de duas páginas, que vira apêndice do protocolo institucional e seção do artigo.

**Como o antibiograma vira recomendação.** Para cada foco, população e setor, listar os esquemas candidatos e a probabilidade de cobertura observada; definir a cobertura mínima desejada por gravidade `[DECIDIR: por exemplo, 90% em sepse, neutropenia febril e meningite; 80% em infecções de menor gravidade]`; escolher o esquema de menor espectro que atinja a meta, respeitando classificação AWaRe, custo, toxicidade e disponibilidade. Registrar a justificativa de cada célula. Esse registro é a base dos itens do Delphi.

**Ferramenta.** O processamento em Python já existente (pandas) é o lugar natural desta etapa; basta acrescentar o identificador de paciente, a regra do primeiro isolado e a estratificação. Recomenda-se versionar o script no repositório e registrar a versão usada em cada tabela.

### Etapa 2. Matriz de recomendações e validação por Delphi

**Objeto da validação.** Duas coisas, em blocos separados do questionário:

- **Bloco 1, recomendações.** Cada célula da matriz (foco × população × setor × condição): antimicrobiano, dose, via, intervalo, duração sugerida, condições de uso, notas. No Hospital Evangélico, parte das células vem do protocolo de março de 2026 e a validação confirma ou ajusta; no Hospital do Câncer, a matriz é nova, derivada da etapa 1 e das diretrizes de neutropenia febril.
- **Bloco 2, ambiguidades.** As 15 lacunas documentadas na transcrição do protocolo do Evangélico (ponto de corte adulto e pediatria; definição de neonatal; critério para azitromicina; escolha entre 1 g e 2 g de cefepima; alternativas na alergia a betalactâmicos; duração; classificação do quinto dia de ventilação; teto de dose pediátrica; peso de referência para aminoglicosídeo; intervalo mínimo de amicacina; infecção comunitária em neonato; nota sobre vancomicina em meningite; dexametasona em meningite; ajuste renal). Cada uma vira um item com opções fechadas mais campo aberto. O Hospital do Câncer recebe o mesmo bloco, adaptado.

**Painel.** Por hospital, 12 a 18 especialistas `[DECIDIR]`, com critérios explícitos: ao menos três anos de prática na instituição ou na área, representação de infectologia, terapia intensiva adulto, pediatria e neonatologia (Evangélico), oncologia clínica e hematologia (Hospital do Câncer), clínica médica, cirurgia, farmácia clínica, microbiologia e enfermagem do SCIH. Convite formal, TCLE eletrônico, anonimato entre os painelistas em todas as rodadas, identificação apenas para a coordenação do estudo.

**Formato dos itens.** Escala de adequação de 1 a 9 (método RAND/UCLA: 1 a 3 inadequado, 4 a 6 incerto, 7 a 9 adequado), com campo de comentário obrigatório para notas 1 a 3.

**Regras de consenso, definidas antes da primeira rodada.** Item aceito quando a mediana é igual ou superior a 7 e ao menos 75% dos painelistas respondem entre 7 e 9, sem desacordo (não mais de 20% das respostas entre 1 e 3). Item rejeitado quando a mediana é igual ou inferior a 3 com os mesmos limiares invertidos. Os demais voltam reformulados na rodada seguinte, com a distribuição das respostas e os comentários anônimos. Máximo de três rodadas; o que não atingir consenso vai a reunião de consenso presencial com registro nominal da decisão do SCIH, e é relatado como tal.

**Prazos.** Duas a três semanas por rodada, com um lembrete; taxa de resposta mínima aceitável de 70% por rodada.

**Validade de conteúdo dos textos do aplicativo.** Para fichas, alertas e mensagens de erro, aplicar índice de validade de conteúdo em clareza e pertinência (escala de 1 a 4; item aceito com IVC igual ou superior a 0,80).

**Relato.** Seguir a diretriz ACCORD (lista de verificação no Anexo B). Os resultados do Delphi são, por si, um artigo.

**Produto.** Matriz de recomendações validada por hospital, com versão e data, assinada pelo SCIH e incorporada ao documento controlado da instituição. Só essa matriz alimenta o aplicativo.

### Etapa 3. Parametrização, verificação e teste formativo do aplicativo

**Princípio.** O protocolo é dado, não código. O motor de decisão é o mesmo nos dois hospitais; muda o pacote de dados (catálogo de fármacos, tabelas por seção, fichas, notas, identidade visual).

**Decisão técnica** `[DECIDIR]`. A instância do Evangélico existe em TypeScript e React, como aplicativo web progressivo que funciona sem internet, não coleta dado de paciente e tem 59 testes que provam que cada célula das tabelas é alcançável e devolve o esquema impresso. A menção a construir em Python merece uma separação de papéis: Python para o processamento do antibiograma e para a análise estatística (etapas 1 e 5), onde já é usado; o motor existente para o aplicativo, porque reescrevê-lo em Python implicaria servidor, perda do funcionamento off-line e repetição de toda a validação técnica. Se a preferência por Python for de manutenção, a parametrização do Hospital do Câncer pode ser feita por arquivos de dados gerados a partir de planilha por um script em Python, sem tocar no motor.

**Passos.**

1. Criar o pacote de dados do Hospital do Câncer a partir da matriz validada; manter em cada regra o campo `textoOriginal` com o texto literal da matriz, para conferência lado a lado.
2. Atualizar o pacote do Evangélico com as decisões do Delphi (bloco 2), com nova versão e data no cabeçalho.
3. Verificação automatizada: para cada instância, testes que provem que toda célula da matriz é alcançável, que cada foco tem exatamente uma opção padrão, que todo fármaco e todo foco referenciados existem, e que as doses ponderais e o ajuste renal reproduzem a matriz. Critério de aceitação: 100% das células, sem exceção.
4. Conferência independente: dois revisores (um farmacêutico e um infectologista), que não escreveram o pacote de dados, percorrem uma lista de cenários que cobre todas as células e comparam a saída do aplicativo com a matriz. Registrar discordâncias, corrigir, repetir até zero discordância. Relatar o número de erros encontrados por rodada.
5. Teste formativo de usabilidade, por hospital, com 6 a 8 prescritores que não participaram do Delphi: cinco tarefas realistas (por exemplo, pneumonia associada à ventilação tardia em adulto; meningite em criança de 3 anos com peso informado; sepse neonatal tardia; paciente com depuração de creatinina reduzida; alergia a betalactâmico), protocolo pensar-em-voz-alta, registro de sucesso na tarefa, tempo, erros e comentários. Corrigir problemas antes da implantação. Participantes assinam TCLE.
6. Controle de versão e de mudança: cada alteração de conteúdo após a implantação exige aprovação do SCIH, nova versão visível no aplicativo e registro no diário do estudo, porque muda a intervenção no meio da série temporal.

**Produto.** Duas instâncias publicadas, cada uma com endereço próprio, ícone e cabeçalho da instituição, relatório de verificação e relatório do teste formativo.

### Etapa 4. Implantação, divulgação e avaliação de usabilidade e alcance

**Pacote de implantação padronizado** (descrever segundo TIDieR):

- Data de lançamento definida e registrada (é o ponto de interrupção da série).
- Apresentação em reunião clínica de cada serviço e nas passagens de plantão; sessão de 15 minutos com demonstração das cinco tarefas do teste formativo.
- Cartazes com código QR nos postos de prescrição, salas de prescrição, UTIs e pronto atendimento; o código aponta para um endereço curto por hospital.
- "Campeões" por unidade (um médico e um farmacêutico), com contato do SCIH para dúvidas e relato de erros.
- Integração ao fluxo existente: a farmácia e o SCIH passam a referenciar o aplicativo ao responder pedidos de antimicrobianos restritos e ao dar feedback de auditoria.
- Lembretes mensais (mural, mensagem institucional) durante os primeiros três meses.

**Medida de alcance sem telemetria no aplicativo.** O aplicativo não coleta dados; para estimar alcance sem alterar isso, usar o contador de acessos do endereço curto por hospital (número agregado de aberturas por mês, sem identificação) e, nas pesquisas de usabilidade, perguntar sobre instalação e frequência de uso. Alternativa `[DECIDIR]`: adicionar ao aplicativo um contador agregado e anônimo de aberturas e de fichas consultadas, sem identificador de dispositivo, descrito no protocolo e no TCLE dos profissionais. A recomendação é a primeira opção; ela preserva a afirmação "nenhum dado sai do aparelho", que simplifica a análise ética e a LGPD.

**Avaliação somativa de usabilidade.** Entre 4 e 8 semanas após o lançamento, convidar todos os prescritores (médicos, residentes) e farmacêuticos de cada hospital, por formulário eletrônico com TCLE: SUS na versão em português do Brasil de Lourenço et al. 2022 `[REF 53]` como instrumento principal; o MAUQ `[REF 54]` não tem versão brasileira localizada, então só entra se a equipe fizer tradução e pré-teste próprios `[DECIDIR: recomendação é usar apenas o SUS e as perguntas abertas]`; três perguntas abertas (o que ajudou, o que atrapalhou, o que falta) e dados profissionais mínimos (categoria, tempo de formado, setor). Meta de resposta: ao menos 30 por hospital. Critério de sucesso: SUS médio igual ou superior a 70. Repetir aos 12 meses para avaliar manutenção.

**Barreiras e facilitadores.** Registrar em diário de implantação, organizado pelos domínios do CFIR, e complementar com entrevistas curtas com os campeões ao fim do período.

### Etapa 5. Conformidade das prescrições empíricas antes e depois

**População.** Prescrições empíricas iniciais de antimicrobianos sistêmicos para as síndromes cobertas pelo protocolo (tabelas 6.1 a 6.6 no Evangélico; matriz equivalente no Hospital do Câncer), em pacientes internados nas unidades cobertas `[DECIDIR: incluir pronto atendimento?]`, adultos e pediátricos, nos dois hospitais.

**Unidade de análise.** O esquema empírico inicial de um episódio de infecção. Um paciente pode contribuir com mais de um episódio se houver novo foco; o segundo episódio só entra após 14 dias do fim do primeiro esquema.

**Inclusão.** Primeiro esquema antimicrobiano prescrito para suspeita de infecção em foco coberto pelo protocolo, iniciado na instituição, no período do estudo.

**Exclusão.** Profilaxia cirúrgica e clínica; terapia dirigida iniciada após resultado de cultura; esquema iniciado em outra instituição e mantido; infecções por patógenos definidos fora do escopo do protocolo (por exemplo, tuberculose, fúngicas, virais); pacientes em cuidados exclusivamente paliativos com decisão documentada de não escalonar.

**Identificação dos casos.** Lista diária ou semanal de novas prescrições de antibacterianos sistêmicos, gerada pela farmácia (sistema de prescrição ou dispensação) ou pelo fluxo de autorização do SCIH. Amostragem `[DECIDIR]`: todos os episódios elegíveis, se o volume mensal for compatível com a capacidade de auditoria; caso contrário, amostra aleatória simples mensal de tamanho fixo por hospital, com sorteio registrado. O tamanho fixo mensal deve garantir os totais da seção 9.

**Coleta.** Extração padronizada por um coletador treinado, no instrumento do Anexo A, em formulário eletrônico com validação de campos. Separação de papéis para reduzir viés: o coletador registra os fatos da prescrição (foco, população, setor, condição, fármacos, dose, via, intervalo, peso, creatinina, horário da prescrição e da primeira dose, culturas, reavaliação); o julgador classifica a conformidade vendo apenas esses fatos e a versão do protocolo vigente na data, sem ver o nome do paciente e, sempre que possível, sem ver a data em si, apenas o código da versão do protocolo aplicável.

**Julgamento da conformidade.** Regras fechadas, por componente, definidas no Anexo A antes da coleta. Classificação em três categorias: conforme; não conforme com justificativa documentada (alergia registrada, cultura prévia conhecida, orientação do SCIH ou da infectologia registrada); não conforme sem justificativa. Desfecho primário `[DECIDIR]`: a recomendação é "conformidade global estrita" (esquema conforme em escolha, dose, via e intervalo, sem contar justificativas), porque é objetiva, reprodutível e é o que o aplicativo influencia diretamente; a "adequação", que soma os desvios justificados, entra como desfecho secundário adjudicado.

**Confiabilidade.** Dois julgadores independentes em amostra aleatória de 15% dos episódios; kappa alvo igual ou superior a 0,80; discordâncias resolvidas por consenso com registro; treinamento prévio com 20 casos até atingir o alvo.

**Períodos.** Pré: 12 meses antes do lançamento (mínimo 8). Período de transição: as 4 semanas seguintes ao lançamento, excluídas da análise primária e incluídas em análise de sensibilidade. Pós: 12 meses após o lançamento.

**Desfechos de balanço e segurança**, descritivos: mortalidade hospitalar dos episódios auditados, transferência para UTI em 48 h, tempo de internação, incidência de *Clostridioides difficile* no período. **Desfecho de controle não equivalente** `[DECIDIR]`: conformidade da profilaxia cirúrgica, que o aplicativo não cobre, medida no mesmo período nos dois hospitais; se ela não mudar enquanto a conformidade da terapia empírica muda, a atribuição ao aplicativo fica mais forte. Isso pressupõe que o projeto de profilaxia só comece depois do período pós deste estudo, ou que comece em unidades diferentes.

---

## 8. Variáveis e desfechos

| Tipo | Variável | Definição operacional | Fonte |
|---|---|---|---|
| Primário | Conformidade global estrita | Escolha do antimicrobiano (1ª ou 2ª opção da matriz para foco, população, setor e condição), dose, via e intervalo conformes; ajuste por peso e por função renal conforme, quando aplicável | Auditoria (Anexo A) |
| Secundário | Conformidade por componente | Cada componente do Anexo A, isoladamente | Auditoria |
| Secundário | Adequação adjudicada | Conforme ou não conforme com justificativa documentada | Auditoria + adjudicação |
| Secundário | Tempo até a primeira dose | Minutos entre a prescrição (ou o registro da suspeita, quando disponível) e a administração da primeira dose; proporção dentro de 1 a 3 h em sepse | Prescrição e registro de enfermagem |
| Secundário | Coleta de culturas antes da 1ª dose | Hemocultura e cultura do sítio coletadas antes da administração | Laboratório e enfermagem |
| Secundário | Reavaliação em 48 a 72 h | Registro médico de reavaliação do esquema com decisão (manter, descalonar, suspender) | Prontuário |
| Secundário | Consumo | DOT por 1.000 pacientes-dia, total e por grupo AWaRe, mensal | Farmácia |
| Secundário | Usabilidade | Escore SUS (0 a 100), por hospital e categoria profissional; MAUQ opcional | Questionário |
| Secundário | Alcance e adoção | Acessos mensais ao endereço por hospital; proporção de respondentes que relatam uso semanal | Encurtador de endereço; questionário |
| Balanço e segurança | Mortalidade hospitalar, UTI em 48 h, permanência, *C. difficile* | Padrão institucional | Prontuário; SCIH |
| Controle | Conformidade da profilaxia cirúrgica | Instrumento próprio do SCIH | Auditoria |
| Covariáveis | Hospital, setor, faixa etária, origem (comunitária ou IRAS), foco, gravidade (UTI, sepse), turno e dia da semana, categoria do prescritor (sem identificação), versão do protocolo vigente, mês | Auditoria |

---

## 9. Tamanho da amostra

**Comparação de proporções (antes versus depois), por hospital.** Bicaudal, alfa de 5%. A conformidade basal `[DADO LOCAL]` substitui a coluna "antes"; a diferença mínima relevante recomendada é de 15 pontos percentuais, compatível com o que se espera de intervenções estruturais de ponto de prescrição. Tabela calculada por fórmula de duas proporções independentes (aproximação normal), número de episódios por período, por hospital:

| Antes | Depois | n por período, poder 80% | n por período, poder 90% |
|---|---|---|---|
| 50% | 65% | 170 | 227 |
| 55% | 70% | 163 | 217 |
| 60% | 75% | 152 | 203 |
| 65% | 80% | 138 | 185 |
| 70% | 85% | 121 | 161 |
| 60% | 70% | 356 | 477 |
| 70% | 80% | 294 | 392 |
| 75% | 85% | 250 | 335 |

Acrescentar 10% por exclusões e registros incompletos. Se a análise primária for por regressão logística com covariáveis, o total acima continua adequado; se houver agrupamento por prescritor ou por unidade, considerar efeito de desenho.

**Série temporal interrompida.** Independentemente da tabela, a série precisa de ao menos 8 pontos mensais por segmento (12 é o recomendado) e de um número de episódios por mês que dê estabilidade à proporção mensal. Com 12 meses antes e 12 depois, 20 a 30 episódios por mês por hospital produzem séries analisáveis e totais entre 240 e 360 por período, acima dos mínimos da tabela para diferenças de 15 pontos.

**Delphi.** 12 a 18 painelistas por hospital, sem cálculo amostral, conforme a literatura de consenso. **Usabilidade.** Formativa com 6 a 8 usuários por hospital; somativa com meta de 30 respondentes por hospital, que dá intervalo de confiança de cerca de 8 pontos em torno da média do SUS, considerando desvio padrão típico.

---

## 10. Análise estatística

1. **Descritiva.** Características dos episódios por hospital e período; conformidade global e por componente, com intervalos de confiança de 95%.
2. **Análise primária.** Diferença de proporções antes versus depois por hospital, com intervalo de 95%; regressão logística com conformidade global como desfecho, período como exposição e ajuste por setor, faixa etária, origem, foco e gravidade; erro padrão robusto agrupado por mês (ou modelo de efeitos mistos com mês como efeito aleatório). Análise conjunta com hospital como efeito fixo e termo de interação período × hospital para testar a H5.
3. **Série temporal interrompida.** Regressão segmentada da proporção mensal de conformidade (ou modelo binomial com os totais mensais), com termos para tendência pré, mudança de nível e mudança de inclinação; verificação de autocorrelação (Durbin-Watson, função de autocorrelação) e correção por Newey-West ou Prais-Winsten; sazonalidade por termos harmônicos se necessário. Relatar efeito absoluto estimado aos 6 e 12 meses após a implantação.
4. **Sensibilidade.** Inclusão do período de transição; exclusão de episódios com justificativa documentada; restrição a UTI; restrição aos focos mais frequentes; análise do desfecho de controle não equivalente.
5. **Secundários.** Componentes por regressão logística; tempo até a primeira dose por mediana e modelo de regressão quantílica ou log-linear; consumo em DOT por série temporal; usabilidade por médias e intervalos, comparação entre hospitais e categorias por modelos lineares.
6. **Delphi.** Mediana, intervalo interquartílico e percentual de concordância por item e rodada; IVC por item e global.
7. **Confiabilidade.** Kappa de Cohen (ou de Fleiss) para conformidade global e por componente.
8. **Dados ausentes.** Análise por casos completos com relato da proporção de perdas por variável; imputação múltipla se as perdas superarem 10% no desfecho primário.
9. **Software.** Python (pandas, statsmodels) ou R; scripts versionados no repositório; relatório reprodutível.
10. **Relato.** TREND para o quase-experimento, SQUIRE 2.0 como complemento de melhoria da qualidade, TIDieR para a intervenção, ACCORD para o Delphi, mERA para o aplicativo, StaRI para a implantação.

---

## 11. Gestão de dados e proteção de dados pessoais

- O aplicativo não coleta, não transmite e não armazena dado de paciente; peso, creatinina e marcos do cronômetro ficam na memória do aparelho. Essa afirmação vai literalmente no protocolo e no TCLE dos profissionais.
- Os dados da auditoria são coletados em formulário eletrônico com controle de acesso; o identificador do paciente é substituído por código sequencial e a tabela de correspondência fica em cada hospital, sob guarda do pesquisador local, separada da base analítica.
- Só a base pseudonimizada circula entre os centros; a base conjunta fica no centro coordenador.
- Bases legais da LGPD: tratamento para realização de estudos por órgão de pesquisa, com pseudonimização sempre que possível; cada hospital é controlador dos dados que originou. O encarregado de dados de cada instituição deve ser informado e o fluxo descrito em um parágrafo do protocolo.
- Guarda dos dados por cinco anos após o término, conforme a Resolução CNS 466/2012, e descarte seguro depois.
- Painel Delphi e questionários de usabilidade: respostas identificadas apenas para a coordenação, análise sempre agregada, relatório sem atribuição individual.

---

## 12. Riscos e benefícios

**Riscos e mitigação.**

- *Erro de conteúdo no aplicativo que induza prescrição inadequada.* Mitigação: conteúdo derivado de documento controlado e validado por consenso; verificação célula a célula; conferência independente; texto original visível em cada esquema; aviso permanente de que prevalece o protocolo na íntegra e o julgamento clínico; canal de relato de erro; controle de versão.
- *Falsa segurança e uso fora do escopo.* Mitigação: o motor recusa combinações não previstas e orienta acionar o SCIH; nada é "melhor palpite".
- *Quebra de confidencialidade de pacientes na auditoria.* Mitigação: pseudonimização, acesso restrito, dispensa de TCLE justificada, TCUD.
- *Constrangimento ou coerção de profissionais.* O pesquisador responsável coordena o SCIH e tem ascendência funcional sobre parte dos prescritores. Mitigação: participação voluntária no Delphi e nas pesquisas, respostas anônimas para a equipe, conformidade analisada por prescrição sem identificação do prescritor, declaração de que os resultados não têm uso disciplinar.
- *Tempo dos participantes.* Delphi: cerca de 40 minutos por rodada; usabilidade: 10 minutos.

**Benefícios.** Diretos para as instituições (protocolo atualizado e validado, ferramenta no ponto de prescrição, medida contínua de conformidade); indiretos para os pacientes (terapia empírica mais adequada, menor exposição a espectro desnecessário); para o sistema de saúde (método transferível e de baixo custo).

---

## 13. Aspectos éticos e regulatórios

- Submissão na Plataforma Brasil pelo Hospital Evangélico como centro coordenador; Hospital do Câncer como centro participante, com Termo de Anuência Institucional e pesquisador responsável local. Pela Lei 14.874/2024 e pelo Despacho Inaep nº 3/2026, a análise ética é única, feita pelo CEP do centro coordenador, que notifica o CEP local `[DECIDIR: confirmar qual CEP está vinculado a cada hospital na Plataforma]`.
- TCLE eletrônico para painelistas do Delphi e para participantes dos testes e questionários de usabilidade, com contatos do CEP responsável e do CEP local.
- Pedido de dispensa de TCLE para a auditoria de prescrições, com justificativa: atividade rotineira do SCIH prevista na Portaria 2.616/1998, inviabilidade de contato com o volume de pacientes, parte com alta ou óbito, risco mínimo, pseudonimização e TCUD. Confirmar com o CEP a posição vigente sobre dispensa após a Lei 14.874/2024 antes de fechar o desenho.
- Declaração de conflito de interesse do pesquisador responsável (autor do protocolo institucional e do aplicativo; coordenador do SCIH).
- Registro no ReBEC antes do início da coleta prospectiva.
- ANVISA RDC 657/2022 e RDC 751/2022: o documento de perguntas e respostas da ANVISA sobre a RDC 657 enquadra como software dispositivo médico a calculadora de bólus e o sistema de apoio à decisão que sugere medicações a partir de protocolos publicados; pela regra de software da RDC 751, apoio à decisão terapêutica tende à classe II. O aplicativo deste projeto tem calculadora de dose por peso e recomenda esquema, então não dá para presumir que está fora do escopo. Conduta: registrar no protocolo a análise de enquadramento, com os atenuantes (uso interno, não comercializado, reprodução literal de documento controlado, decisão final do prescritor, sem dado de paciente persistido), e solicitar posicionamento formal à ANVISA ou à área regulatória da instituição antes da implantação `[DECIDIR]`. O CEP pode perguntar; a resposta precisa estar escrita.
- O cronograma de coleta começa somente após a aprovação ética.

---

## 14. Cronograma proposto

Mês 0 é a submissão ao CEP. Os meses negativos são o período basal, já auditado ou a reauditar.

| Período | Atividade | Etapa |
|---|---|---|
| M-12 a M-1 | Linha de base de conformidade (existente; harmonizar) | 0 |
| M0 | Submissão ao CEP; registro ReBEC após aprovação | 13 |
| M1 a M2 | Antibiograma cumulativo dos dois hospitais; matriz preliminar do Hospital do Câncer; itens do Delphi | 1 e 2 |
| M3 a M5 | Delphi (até 3 rodadas) e IVC dos textos | 2 |
| M5 a M6 | Pacotes de dados, verificação, conferência independente, teste formativo | 3 |
| M7 | Lançamento no Hospital Evangélico | 4 |
| M9 | Lançamento no Hospital do Câncer (se escalonado) | 4 |
| M8 a M9 e M10 a M11 | Usabilidade somativa em cada hospital | 4 |
| M7 a M20 | Auditoria mensal de conformidade (12 meses pós em cada hospital) | 5 |
| M19 e M21 | Repetição da usabilidade aos 12 meses | 4 |
| M21 a M23 | Análise, relatório final ao CEP | 10 |
| M12, M24 | Relatórios parciais e final na Plataforma Brasil | 13 |
| M22 a M26 | Manuscritos (Delphi e protocolo local; desenvolvimento e usabilidade; efeito sobre a conformidade) | 17 |

---

## 15. Orçamento (itens; valores a preencher)

| Item | Uso | Valor |
|---|---|---|
| Formulário eletrônico de coleta (REDCap institucional ou equivalente) | Auditoria, Delphi, usabilidade | `[preencher]` |
| Hospedagem das instâncias do aplicativo e domínio | Etapas 3 e 4 | `[preencher]` (planos gratuitos atendem) |
| Impressão de cartazes com QR | Etapa 4 | `[preencher]` |
| Horas de coletador e julgadores | Etapa 5 | `[preencher]` |
| Licença de software estatístico, se não usar R ou Python | Etapa 10 | `[preencher]` |
| Tradução e taxas de publicação | Etapa 17 | `[preencher]` |

---

## 16. Equipe e responsabilidades

| Papel | Responsabilidade | Nome |
|---|---|---|
| Pesquisador responsável e centro coordenador | Desenho, conteúdo do Evangélico, análise, relatórios | Dr. Philipe Bellinati |
| Pesquisador responsável local, Hospital do Câncer | Anuência, matriz local, coleta local | `[DADO LOCAL]` |
| Farmacêutico clínico (por hospital) | Antibiograma, matriz, coleta, julgamento | `[DADO LOCAL]` |
| Microbiologista (por hospital) | Exportação e regras do antibiograma | `[DADO LOCAL]` |
| Desenvolvedor / mantenedor do aplicativo | Pacotes de dados, testes, publicação | `[DADO LOCAL]` |
| Estatístico ou epidemiologista | Amostra, série temporal, relatório | `[DADO LOCAL]` |
| Campeões por unidade | Divulgação e feedback | `[DADO LOCAL]` |

---

## 17. Produtos esperados e divulgação

1. Antibiograma cumulativo anual e nota metodológica em cada hospital (produto institucional).
2. Protocolo de antibioticoterapia empírica do Hospital do Câncer, validado por consenso, e protocolo revisado do Evangélico com as ambiguidades resolvidas (documentos controlados).
3. Duas instâncias publicadas do aplicativo, com relatório de verificação.
4. Instrumento de auditoria de conformidade reutilizável (Anexo A).
5. Artigos: (a) derivação e validação por Delphi de protocolo empírico a partir do antibiograma local em hospital oncológico; (b) desenvolvimento, verificação e usabilidade de aplicativo parametrizável de antibioticoterapia empírica; (c) efeito da implantação sobre a conformidade em dois hospitais, com série temporal interrompida.
6. Apresentação dos resultados às CCIHs, às diretorias clínicas e às equipes participantes.

---

## 18. Limitações antecipadas

- Ausência de randomização; tendência secular e cointervenções mitigadas por série temporal, dois hospitais, escalonamento e desfecho de controle.
- Efeito Hawthorne da auditoria, presente nos dois períodos se a linha de base já era auditada, o que reduz o viés diferencial.
- Contaminação entre hospitais por prescritores comuns; estimar a proporção e analisar sensibilidade.
- Uso do aplicativo não medido individualmente (sem telemetria); alcance estimado por acessos agregados e autorrelato.
- Cegamento parcial dos julgadores.
- Conformidade é desfecho de processo; desfechos clínicos entram apenas como balanço.
- Generalização restrita a hospitais com SCIH estruturado e protocolo vigente.

---

## 19. Decisões pendentes do pesquisador responsável

| # | Decisão | Recomendação registrada |
|---|---|---|
| 1 | Tecnologia do aplicativo: manter o motor existente ou reescrever em Python | Manter o motor; Python para antibiograma e análise |
| 2 | Desfecho primário: conformidade estrita ou adequação com desvios justificados | Conformidade estrita como primário; adequação como secundário |
| 3 | Lançamento simultâneo ou escalonado | Escalonado, com dois a três meses de intervalo |
| 4 | Telemetria agregada no aplicativo | Não; usar contador do endereço curto e autorrelato |
| 5 | Linha de base: reutilizar como está ou reauditar amostra | Reauditar amostra se o instrumento diferir do Anexo A |
| 6 | Escopo: incluir pronto atendimento; incluir pediatria no Hospital do Câncer | Incluir onde o protocolo local cobre |
| 7 | Desfecho de controle: conformidade da profilaxia cirúrgica | Sim, e sequenciar o projeto de profilaxia depois do período pós |
| 8 | Metas de cobertura por gravidade na derivação das recomendações | 90% para sepse, neutropenia febril e meningite; 80% nos demais |
| 9 | Tamanho do painel Delphi por hospital | 12 a 18 |
| 10 | CEP vinculado a cada hospital na Plataforma Brasil | Confirmar antes da submissão |
| 11 | Instrumento de usabilidade | SUS em português do Brasil e perguntas abertas; MAUQ só com tradução própria |
| 12 | Enquadramento regulatório do aplicativo (RDC 657/2022) | Documentar a análise e solicitar posicionamento formal antes da implantação |

---

## 20. Referências

Lista consolidada. `[VERIFICADO]` significa PMID e DOI conferidos no PubMed em 10/09/2026; `[WEB]` significa documento não indexado, localizado por busca na internet. Quando o título aparece entre colchetes, é uma descrição do conteúdo, e o título exato deve ser copiado do registro PMID ao formatar no gerenciador de referências. Numeração citada no texto como `[REF n]`.

**Resistência antimicrobiana, IRAS e política pública**

1. Antimicrobial Resistance Collaborators (Murray CJL et al.). Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629-655. PMID 35065702; DOI 10.1016/S0140-6736(21)02724-0. `[VERIFICADO]`
2. ANVISA. Diretriz Nacional para Elaboração de Programa de Gerenciamento do Uso de Antimicrobianos em Serviços de Saúde. Brasília; 2017, versão revisada 2023. `[WEB]`
3. ANVISA. Programa Nacional de Prevenção e Controle de Infecções Relacionadas à Assistência à Saúde (PNPCIRAS) 2021-2025 (Portaria ANVISA 143/2021). Citar a versão vigente na data da submissão; a versão 2026-2030 já foi aprovada. `[WEB]`
4. Brasil. Ministério da Saúde. Portaria GM/MS nº 2.616, de 12 de maio de 1998. `[WEB]`
5. Centers for Disease Control and Prevention. Core Elements of Hospital Antibiotic Stewardship Programs. Atlanta; 2019. `[WEB]`
6. World Health Organization. AWaRe classification of antibiotics for evaluation and monitoring of use, 2023 (WHO/MHP/HPS/EML/2023.04); The WHO AWaRe Antibiotic Book, 2022 (WHO/MHP/HPS/EML/2022.02). `[WEB]`
7. Moja L, Zanichelli V, Mertz D, et al. WHO's essential medicines and AWaRe: recommendations on first- and second-choice antibiotics for empiric treatment of clinical infections. Clin Microbiol Infect. 2024;30(Suppl 2):S1-S51. PMID 38342438; DOI 10.1016/j.cmi.2024.02.003. `[VERIFICADO]`

**Gerenciamento do uso de antimicrobianos**

8. Barlam TF, Cosgrove SE, Abbo LM, et al. Implementing an antibiotic stewardship program: guidelines by the Infectious Diseases Society of America and the Society for Healthcare Epidemiology of America. Clin Infect Dis. 2016;62(10):e51-e77. PMID 27080992; DOI 10.1093/cid/ciw118. `[VERIFICADO]` (sumário executivo: PMID 27118828; DOI 10.1093/cid/ciw217)
9. Davey P, Marwick CA, Scott CL, et al. Interventions to improve antibiotic prescribing practices for hospital inpatients. Cochrane Database Syst Rev. 2017;2:CD003543. PMID 28178770; DOI 10.1002/14651858.CD003543.pub4. `[VERIFICADO]`

**Aplicativos e sistemas de apoio à decisão em antimicrobianos**

10. Charani E, Kyratsis Y, Lawson W, et al. An analysis of the development and implementation of a smartphone application for the delivery of antimicrobial prescribing policy: lessons learnt. J Antimicrob Chemother. 2013;68(4):960-967. PMID 23258314; DOI 10.1093/jac/dks492. `[VERIFICADO]`
11. Panesar P, Jones A, Aldous A, et al. Attitudes and behaviours to antimicrobial prescribing following introduction of a smartphone app. PLoS One. 2016;11(4):e0154202. PMID 27111775; DOI 10.1371/journal.pone.0154202. `[VERIFICADO]`
12. Tuon FF, Gasparetto J, Wollmann LC, et al. Mobile health application to assist doctors in antibiotic prescription: an approach for antibiotic stewardship. Braz J Infect Dis. 2017;21(6):660-664. PMID 28941393; DOI 10.1016/j.bjid.2017.08.002. `[VERIFICADO]`
13. Helou RI, Foudraine DE, Catho G, et al. Use of stewardship smartphone applications by physicians and prescribing of antimicrobials in hospitals: a systematic review. PLoS One. 2020;15(9):e0239751. PMID 32991591; DOI 10.1371/journal.pone.0239751. `[VERIFICADO]`
14. Baysari MT, Lehnbom EC, Li L, et al. The effectiveness of information technology to improve antimicrobial prescribing in hospitals: a systematic review and meta-analysis. Int J Med Inform. 2016;92:15-34. PMID 27318068; DOI 10.1016/j.ijmedinf.2016.04.008. `[VERIFICADO]`
15. Curtis CE, Al Bahar F, Marriott JF. The effectiveness of computerised decision support on antibiotic use in hospitals: a systematic review. PLoS One. 2017;12(8):e0183062. PMID 28837665; DOI 10.1371/journal.pone.0183062. `[VERIFICADO]`
16. Rittmann B, Stevens MP. Clinical decision support systems and their role in antibiotic stewardship: a systematic review. Curr Infect Dis Rep. 2019;21(8):29. PMID 31342180; DOI 10.1007/s11908-019-0683-8. `[VERIFICADO]`
17. Helou RI, Catho G, Faxén L, et al. [Ensaio randomizado escalonado multicêntrico de aplicativo de stewardship com diretrizes locais; desfecho de terapia apropriada]. Clin Microbiol Infect. 2025;31(7):1172-1179. PMID 40032084; DOI 10.1016/j.cmi.2025.02.026. `[VERIFICADO]`
18. Chansamouth V, Chommanam D, Lee SJ, et al. [Ensaio randomizado escalonado em hospitais do Laos: adesão a diretrizes de antimicrobianos entregues por aplicativo versus papel]. PLoS Med. 2026;23(8):e1005205. PMID 42659762; DOI 10.1371/journal.pmed.1005205. `[VERIFICADO]`
19. Tuon FF, Zequinao T, da Silva MS, et al. [Revisão sistemática e metanálise brasileira sobre eHealth e mHealth e adequação da terapia empírica]. Infect Dis Rep. 2024;16(4):707-723. PMID 39195005; DOI 10.3390/idr16040054. `[VERIFICADO]`
20. Yoon CH, Nolan I, Humphrey G, et al. [Série temporal interrompida: adesão sustentada a diretrizes com aplicativo de antimicrobianos]. J Med Internet Res. 2023;25:e42978. PMID 37129941; DOI 10.2196/42978. `[VERIFICADO]`

**Medida de conformidade e adequação**

21. Spivak ES, Cosgrove SE, Srinivasan A. Measuring appropriate antimicrobial use: attempts at opening the black box. Clin Infect Dis. 2016;63(12):1639-1644. PMID 27682070; DOI 10.1093/cid/ciw658. `[VERIFICADO]`
22. DePestel DD, Eiland EH 3rd, Lusardi K, et al. Assessing appropriateness of antimicrobial therapy: in the eye of the interpreter. Clin Infect Dis. 2014;59(Suppl 3):S154-S161. PMID 25261542; DOI 10.1093/cid/ciu548. `[VERIFICADO]`
23. Versporten A, Zarb P, Caniaux I, et al. Antimicrobial consumption and resistance in adult hospital inpatients in 53 countries: results of an internet-based global point prevalence survey. Lancet Glob Health. 2018;6(6):e619-e629. PMID 29681513; DOI 10.1016/S2214-109X(18)30186-4. `[VERIFICADO]`
24. Porto APM, Goossens H, Versporten A, et al. Global point prevalence survey of antimicrobial consumption in Brazilian hospitals. J Hosp Infect. 2020;104(2):165-171 (publicado on-line em 2019). PMID 31678430; DOI 10.1016/j.jhin.2019.10.016. `[VERIFICADO]`
25. Cambiais AMVB, Pinto VB, Sforsin ACP, et al. [Auditoria de prescrição de antimicrobianos pelos "quatro momentos" em hospital universitário brasileiro]. Antimicrob Resist Infect Control. 2026;15(1). PMID 42286698; DOI 10.1186/s13756-026-01761-4. `[VERIFICADO]`
26. Raniero JTMW, Cortez AC, Costa CMLD, et al. [Adesão a protocolo de neutropenia febril em hospital oncológico brasileiro]. Pediatr Hematol Oncol. 2025;42(6-7):312-322. PMID 40590388; DOI 10.1080/08880018.2025.2525267. `[VERIFICADO]`

**Determinantes comportamentais da prescrição**

27. Charani E, Castro-Sánchez E, Sevdalis N, et al. Understanding the determinants of antimicrobial prescribing within hospitals: the role of "prescribing etiquette". Clin Infect Dis. 2013;57(2):188-196. PMID 23572483; DOI 10.1093/cid/cit212. `[VERIFICADO]`
28. Hulscher MEJL, Grol RPTM, van der Meer JWM. Antibiotic prescribing in hospitals: a social and behavioural scientific approach. Lancet Infect Dis. 2010;10(3):167-175. PMID 20185095; DOI 10.1016/S1473-3099(10)70027-X. `[VERIFICADO]`
29. Michie S, van Stralen MM, West R. The behaviour change wheel: a new method for characterising and designing behaviour change interventions. Implement Sci. 2011;6:42. PMID 21513547; DOI 10.1186/1748-5908-6-42. `[VERIFICADO]`

**Oncologia e neutropenia febril**

30. Freifeld AG, Bow EJ, Sepkowitz KA, et al. Clinical practice guideline for the use of antimicrobial agents in neutropenic patients with cancer: 2010 update by the Infectious Diseases Society of America. Clin Infect Dis. 2011;52(4):e56-e93. PMID 21258094; DOI 10.1093/cid/cir073. `[VERIFICADO]`
31. Taplitz RA, Kennedy EB, Bow EJ, et al. Outpatient management of fever and neutropenia in adults treated for malignancy: ASCO and IDSA clinical practice guideline update. J Clin Oncol. 2018;36(14):1443-1453. PMID 29461916; DOI 10.1200/JCO.2017.77.6211. `[VERIFICADO]`
32. Klastersky J, de Naurois J, Rolston K, et al. Management of febrile neutropaenia: ESMO clinical practice guidelines. Ann Oncol. 2016;27(suppl 5):v111-v118. PMID 27664247; DOI 10.1093/annonc/mdw325. `[VERIFICADO]`
33. Averbuch D, Orasch C, Cordonnier C, et al. European guidelines for empirical antibacterial therapy for febrile neutropenic patients in the era of growing resistance: summary of the 2011 4th European Conference on Infections in Leukemia. Haematologica. 2013;98(12):1826-1835. PMID 24323983; DOI 10.3324/haematol.2013.091025. `[VERIFICADO]`
34. Nucci M, Arrais-Rodrigues C, Bergamasco MD, et al. [Consenso da ABHH sobre neutropenia febril, por método Delphi]. Hematol Transfus Cell Ther. 2024;46(Suppl 6):S346-S361. PMID 39694764; DOI 10.1016/j.htct.2024.11.119. `[VERIFICADO]`
35. Schonardie AP, Beck E, Rigatto MH. [Patógenos de infecção de corrente sanguínea e preditores de bacilos gram-negativos resistentes a carbapenêmicos em neutropenia febril, Porto Alegre]. Braz J Infect Dis. 2023;27(2):102758. PMID 36809849; DOI 10.1016/j.bjid.2023.102758. `[VERIFICADO]`
36. de Souza ILA, Cappellano P, Ferreira DB, et al. [Enterobactérias produtoras de KPC em pacientes hematológicos e transplantados, coorte brasileira de 10 anos]. PLoS One. 2024;19(1):e0297161. PMID 38277372; DOI 10.1371/journal.pone.0297161. `[VERIFICADO]`

**Antibiograma cumulativo e epidemiologia local**

37. Clinical and Laboratory Standards Institute. M39: Analysis and Presentation of Cumulative Antimicrobial Susceptibility Test Data. 5th ed. Wayne, PA; 2022. `[WEB]`
38. Brazilian Committee on Antimicrobial Susceptibility Testing (BrCAST). Tabelas de pontos de corte clínicos BrCAST-EUCAST, versão vigente (a partir de 01/02/2025). `[WEB]`
39. Hindler JF, Stelling J. Analysis and presentation of cumulative antibiograms: a new consensus guideline from the Clinical and Laboratory Standards Institute. Clin Infect Dis. 2007;44(6):867-873. PMID 17304462; DOI 10.1086/511864. `[VERIFICADO]`
40. Hebert C, Ridgway J, Vekhter B, et al. Demonstration of the weighted-incidence syndromic combination antibiogram: an empiric prescribing decision aid. Infect Control Hosp Epidemiol. 2012;33(4):381-388. PMID 22418634; DOI 10.1086/664768. `[VERIFICADO]`

**Delphi, consenso e validade de conteúdo**

41. Diamond IR, Grant RC, Feldman BM, et al. Defining consensus: a systematic review recommends methodologic criteria for reporting of Delphi studies. J Clin Epidemiol. 2014;67(4):401-409. PMID 24581294; DOI 10.1016/j.jclinepi.2013.12.002. `[VERIFICADO]`
42. Nasa P, Jain R, Juneja D. Delphi methodology in healthcare research: how to decide its appropriateness. World J Methodol. 2021;11(4):116-129. PMID 34322364; DOI 10.5662/wjm.v11.i4.116. `[VERIFICADO]`
43. Hsu CC, Sandford BA. The Delphi technique: making sense of consensus. Pract Assess Res Eval. 2007;12(10):1-8. DOI 10.7275/pdz9-th90. `[WEB]`
44. Jünger S, Payne SA, Brine J, et al. Guidance on Conducting and REporting DElphi Studies (CREDES) in palliative care: recommendations based on a methodological systematic review. Palliat Med. 2017;31(8):684-706. PMID 28190381; DOI 10.1177/0269216317690685. `[VERIFICADO]`
45. Gattrell WT, Logullo P, van Zuuren EJ, et al. ACCORD (ACcurate COnsensus Reporting Document): a reporting guideline for consensus methods in biomedicine developed via a modified Delphi. PLoS Med. 2024;21(1):e1004326. PMID 38261576; DOI 10.1371/journal.pmed.1004326. `[VERIFICADO]` Explicação e elaboração: Logullo P, et al. PLoS Med. 2024;21(5):e1004390. PMID 38709851; DOI 10.1371/journal.pmed.1004390. `[VERIFICADO]`
46. Fitch K, Bernstein SJ, Aguilar MD, et al. The RAND/UCLA Appropriateness Method User's Manual. Santa Monica: RAND; 2001. MR-1269. `[WEB]`
47. Rocha DM, Oliveira AC, Bezerra SMG, et al. [Validação de aplicativo em saúde por técnica Delphi e índice de validade de conteúdo, Brasil]. Int J Environ Res Public Health. 2025;22(7):1115. PMID 40724181; DOI 10.3390/ijerph22071115. `[VERIFICADO]`
48. Polit DF, Beck CT. The content validity index: are you sure you know what's being reported? Critique and recommendations. Res Nurs Health. 2006;29(5):489-497. PMID 16977646; DOI 10.1002/nur.20147. `[VERIFICADO]`
49. Lynn MR. Determination and quantification of content validity. Nurs Res. 1986;35(6):382-385. PMID 3640358. `[VERIFICADO; DOI 10.1097/00006199-198611000-00017 apenas por busca web]`
50. Alexandre NMC, Coluci MZO. Validade de conteúdo nos processos de construção e adaptação de instrumentos de medidas. Ciênc Saúde Coletiva. 2011;16(7):3061-3068. PMID 21808894; DOI 10.1590/S1413-81232011000800006. `[VERIFICADO]`

**Usabilidade**

51. Brooke J. SUS: a "quick and dirty" usability scale. In: Jordan PW, Thomas B, Weerdmeester BA, McClelland IL, eds. Usability Evaluation in Industry. London: Taylor & Francis; 1996:189-194. DOI 10.1201/9781498710411-35. `[WEB]`
52. Lewis JR. The System Usability Scale: past, present, and future. Int J Hum Comput Interact. 2018;34(7):577-590. DOI 10.1080/10447318.2018.1455307. `[WEB]`
53. Lourenço DF, Carmona EV, Lopes MHBM. Tradução e adaptação transcultural da System Usability Scale para o português do Brasil. Aquichan. 2022;22(2):e2228. DOI 10.5294/aqui.2022.22.2.8. `[WEB]`
54. Zhou L, Bao J, Setiawan IMA, et al. The mHealth App Usability Questionnaire (MAUQ): development and validation study. JMIR Mhealth Uhealth. 2019;7(4):e11500. PMID 30973342; DOI 10.2196/11500. `[VERIFICADO]` Versão brasileira validada: não localizada em 10/09/2026.
55. Stoyanov SR, Hides L, Kavanagh DJ, Zelenko O. Development and validation of the user version of the Mobile Application Rating Scale (uMARS). JMIR Mhealth Uhealth. 2016;4(2):e72. PMID 27287964; DOI 10.2196/mhealth.5849. `[VERIFICADO]`
56. Nielsen J, Landauer TK. A mathematical model of the finding of usability problems. Proc INTERCHI '93. 1993:206-213. DOI 10.1145/169059.169166. `[WEB]`
57. International Organization for Standardization. ISO 9241-11:2018. Ergonomics of human-system interaction, Part 11: Usability: definitions and concepts. Geneva; 2018. `[WEB]`

**Desenho quase-experimental e análise**

58. Bernal JL, Cummins S, Gasparrini A. Interrupted time series regression for the evaluation of public health interventions: a tutorial. Int J Epidemiol. 2017;46(1):348-355. PMID 27283160; DOI 10.1093/ije/dyw098. `[VERIFICADO]`
59. Wagner AK, Soumerai SB, Zhang F, Ross-Degnan D. Segmented regression analysis of interrupted time series studies in medication use research. J Clin Pharm Ther. 2002;27(4):299-309. PMID 12174032; DOI 10.1046/j.1365-2710.2002.00430.x. `[VERIFICADO]`
60. Penfold RB, Zhang F. Use of interrupted time series analysis in evaluating health care quality improvements. Acad Pediatr. 2013;13(6 Suppl):S38-S44. PMID 24268083; DOI 10.1016/j.acap.2013.08.002. `[VERIFICADO]`
61. Harris AD, Bradham DD, Baumgarten M, et al. The use and interpretation of quasi-experimental studies in infectious diseases. Clin Infect Dis. 2004;38(11):1586-1591. PMID 15156447; DOI 10.1086/420936. `[VERIFICADO]`
62. Shardell M, Harris AD, El-Kamary SS, et al. Statistical analysis and application of quasi experiments to antimicrobial resistance intervention studies. Clin Infect Dis. 2007;45(7):901-907. PMID 17806059; DOI 10.1086/521255. `[VERIFICADO]`
63. Schweitzer VA, van Werkhoven CH, Rodríguez Baño J, et al. Optimizing design of research to evaluate antibiotic stewardship interventions: consensus recommendations of a multinational working group. Clin Microbiol Infect. 2020;26(1):41-50. PMID 31493472; DOI 10.1016/j.cmi.2019.08.017. `[VERIFICADO]`
64. Hemming K, Haines TP, Chilton PJ, et al. The stepped wedge cluster randomised trial: rationale, design, analysis, and reporting. BMJ. 2015;350:h391. PMID 25662947; DOI 10.1136/bmj.h391. `[VERIFICADO]`

**Diretrizes de relato**

65. Des Jarlais DC, Lyles C, Crepaz N; TREND Group. Improving the reporting quality of nonrandomized evaluations of behavioral and public health interventions: the TREND statement. Am J Public Health. 2004;94(3):361-366. PMID 14998794; DOI 10.2105/ajph.94.3.361. `[VERIFICADO]`
66. Ogrinc G, Davies L, Goodman D, et al. SQUIRE 2.0 (Standards for QUality Improvement Reporting Excellence): revised publication guidelines from a detailed consensus process. BMJ Qual Saf. 2016;25(12):986-992. PMID 26369893; DOI 10.1136/bmjqs-2015-004411. `[VERIFICADO]`
67. Agarwal S, LeFevre AE, Lee J, et al. Guidelines for reporting of health interventions using mobile phones: mobile health (mHealth) evidence reporting and assessment (mERA) checklist. BMJ. 2016;352:i1174. PMID 26988021; DOI 10.1136/bmj.i1174. `[VERIFICADO]`
68. Hoffmann TC, Glasziou PP, Boutron I, et al. Better reporting of interventions: template for intervention description and replication (TIDieR) checklist and guide. BMJ. 2014;348:g1687. PMID 24609605; DOI 10.1136/bmj.g1687. `[VERIFICADO]`
69. Pinnock H, Barwick M, Carpenter CR, et al. Standards for Reporting Implementation Studies (StaRI) Statement. BMJ. 2017;356:i6795. PMID 28264797; DOI 10.1136/bmj.i6795. `[VERIFICADO]`

**Ciência da implementação**

70. Damschroder LJ, Aron DC, Keith RE, et al. Fostering implementation of health services research findings into practice: a consolidated framework for advancing implementation science. Implement Sci. 2009;4:50. PMID 19664226; DOI 10.1186/1748-5908-4-50. `[VERIFICADO]`
71. Damschroder LJ, Reardon CM, Widerquist MAO, Lowery J. The updated Consolidated Framework for Implementation Research based on user feedback. Implement Sci. 2022;17(1):75. PMID 36309746; DOI 10.1186/s13012-022-01245-0. `[VERIFICADO]`
72. Proctor E, Silmere H, Raghavan R, et al. Outcomes for implementation research: conceptual distinctions, measurement challenges, and research agenda. Adm Policy Ment Health. 2011;38(2):65-76. PMID 20957426; DOI 10.1007/s10488-010-0319-7. `[VERIFICADO]`
73. Glasgow RE, Vogt TM, Boles SM. Evaluating the public health impact of health promotion interventions: the RE-AIM framework. Am J Public Health. 1999;89(9):1322-1327. PMID 10474547; DOI 10.2105/ajph.89.9.1322. `[VERIFICADO]`

**Ética, proteção de dados e regulação**

74. Brasil. Lei nº 14.874, de 28 de maio de 2024. Dispõe sobre a pesquisa com seres humanos e institui o Sistema Nacional de Ética em Pesquisa com Seres Humanos. `[WEB]`
75. Brasil. Decreto nº 12.651, de 7 de outubro de 2025. Regulamenta a Lei nº 14.874/2024. `[WEB]`
76. Instância Nacional de Ética em Pesquisa (Inaep). Despacho nº 2/2026 (prazos de tramitação) e Despacho nº 3/2026 (análise ética única em pesquisas multicêntricas). `[WEB]`
77. Conselho Nacional de Saúde. Resolução nº 466, de 12 de dezembro de 2012; Resolução nº 674, de 6 de maio de 2022. `[WEB]`
78. Brasil. Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais), art. 7º, IV; art. 11, II, c; art. 13. `[WEB]`
79. ANVISA. RDC nº 657, de 24 de março de 2022 (software como dispositivo médico); RDC nº 751, de 15 de setembro de 2022 (classificação de risco e regularização de dispositivos médicos); Perguntas e Respostas sobre a RDC 657/2022, versão 1, 2022. `[WEB]`
80. Conselho Federal de Medicina. Resolução CFM nº 2.299/2021 (documentos médicos eletrônicos); Resolução CFM nº 2.314/2022 (telemedicina). `[WEB]`

---

## Anexo A. Instrumento de auditoria de conformidade da prescrição empírica

Os componentes seguem a lógica dos "quatro momentos" da decisão antimicrobiana (indicação e culturas; escolha empírica; reavaliação; duração), usada em auditoria recente em hospital brasileiro `[REF 25]`, e a definição operacional de uso apropriado de Spivak et al. `[REF 21]`.

**Bloco 1, identificação (coletador).** Código do episódio; hospital; setor; data e hora da prescrição; faixa etária (neonatal até 28 dias, pediátrico, adulto); peso registrado (kg); creatinina e depuração estimada, se disponíveis; origem (comunitária ou IRAS); foco e condição conforme a matriz (por exemplo, "PAV tardia", "ITU associada a cateter"); gravidade (sepse, UTI); alergia registrada a betalactâmico; cultura prévia com resultado conhecido; versão do protocolo vigente na data.

**Bloco 2, prescrição (coletador).** Para cada antimicrobiano do esquema: nome, dose, unidade, via, intervalo, data e hora da primeira dose administrada; associações e itens facultativos; registro de autorização do SCIH quando restrito; hemocultura e cultura do sítio coletadas antes da primeira dose (sim, não, sem registro); registro de reavaliação em 48 a 72 h com decisão; duração planejada, se registrada.

**Bloco 3, julgamento (julgador, cego ao nome e, quando possível, à data).**

| Componente | Regra de conformidade | Resultado |
|---|---|---|
| C1 Escolha do antimicrobiano | Esquema igual à 1ª ou 2ª opção da matriz para foco, população, setor e condição; associações facultativas não contam contra; item obrigatório ausente conta contra | Conforme / Não conforme |
| C2 Dose | Dentro da faixa da matriz; em pediatria, mg/kg dentro da faixa, sem ultrapassar o teto adulto; ajuste renal conforme a tabela quando a depuração exige | Conforme / Não conforme / Não aplicável |
| C3 Via | Igual à da matriz | Conforme / Não conforme |
| C4 Intervalo | Igual ao da matriz, considerando o ajuste renal | Conforme / Não conforme |
| C5 Culturas antes da 1ª dose | Hemocultura (e cultura do sítio quando aplicável) coletadas antes da administração | Conforme / Não conforme / Sem registro |
| C6 Tempo até a 1ª dose | Dentro da janela do protocolo (1 a 3 h) em sepse; registrado em minutos nos demais | Minutos; Conforme / Não conforme quando aplicável |
| C7 Reavaliação em 48 a 72 h | Registro médico de reavaliação com decisão | Conforme / Não conforme |
| C8 Antimicrobiano restrito | Autorização do SCIH registrada quando exigida | Conforme / Não conforme / Não aplicável |
| Conformidade global estrita | C1, C2, C3 e C4 conformes (C2 e C4 avaliados após ajuste renal quando aplicável) | Sim / Não |
| Justificativa documentada para desvio | Alergia registrada; cultura prévia; orientação da infectologia ou do SCIH registrada | Sim / Não |
| Adequação adjudicada | Conformidade global estrita OU desvio com justificativa aceita pelo julgador | Sim / Não |

Regras adicionais a fixar antes da coleta: tolerância de arredondamento de dose (por exemplo, 10%); como tratar dose "1 a 2 g" quando a matriz não define o critério; o que fazer quando faltar peso em pediatria (C2 "sem registro", conta como não conforme na análise primária e como ausente na de sensibilidade).

## Anexo B. Roteiro do Delphi

1. **Preparação.** Lista de itens do bloco 1 (uma linha por célula da matriz, com a justificativa derivada do antibiograma) e do bloco 2 (ambiguidades A-01 a A-15 adaptadas). Piloto do questionário com dois especialistas fora do painel para clareza e tempo de resposta.
2. **Convite e consentimento.** Carta com objetivos, número previsto de rodadas, tempo estimado, anonimato e TCLE eletrônico.
3. **Rodada 1.** Escala 1 a 9 por item; comentário obrigatório para 1 a 3; sugestão de itens novos ao final.
4. **Análise entre rodadas.** Mediana, intervalo interquartílico, percentual em 7 a 9 e em 1 a 3; classificação aceito, rejeitado, reformular; síntese anônima dos comentários.
5. **Rodada 2 e 3.** Só itens reformulados e itens novos, com a distribuição anterior visível.
6. **Reunião de consenso.** Itens remanescentes; decisão nominal do SCIH registrada e relatada como decisão de comitê, não como consenso Delphi.
7. **Relato.** Lista de verificação ACCORD: justificativa do método, seleção do painel, definição prévia de consenso, número de rodadas, taxas de resposta, resultados por item, mudanças entre rodadas, conflitos de interesse.

## Anexo C. Itens da System Usability Scale

Usar a versão brasileira validada citada na seção 20; os dez itens alternam afirmações positivas e negativas em escala de 1 (discordo totalmente) a 5 (concordo totalmente) e o escore final vai de 0 a 100. Referência de interpretação: 68 é a média histórica; 70 ou mais indica usabilidade aceitável. Acrescentar ao formulário: categoria profissional, tempo de formado, setor, frequência de uso do aplicativo na última semana, e três perguntas abertas.

## Anexo D. Estrutura de dados para o antibiograma cumulativo

Campos mínimos da exportação, por linha (um resultado de antimicrobiano por isolado): identificador pseudonimizado do paciente; código da ordem de serviço; data da coleta; unidade de coleta; material; microrganismo; antimicrobiano; classificação (sensível, intermediário ou sensível aumentado, resistente); observações do isolado (para polimixina B); indicador de cultura de vigilância.

Regras de processamento, na ordem: remover negativos e triagens; padronizar nomes de microrganismos; extrair polimixina B das observações; remover duplicatas exatas (ordem de serviço, microrganismo, antimicrobiano); aplicar primeiro isolado por paciente, espécie e período (ou por setor, se estratificado); contar isolados testados por droga; calcular percentual de sensíveis apenas onde n é igual ou superior a 30; marcar estimativas com n menor; gerar tabelas por setor e material e antibiogramas sindrômicos; registrar versão do script, data e pontos de corte.

## Anexo E. Modelo da matriz de recomendações por hospital

Uma linha por célula: seção (população × origem × setor); foco; condição; prioridade da regra; 1ª opção (fármaco, dose, via, intervalo); 2ª opção; itens facultativos com critério; duração sugerida; notas de rodapé; probabilidade de cobertura estimada no antibiograma local; justificativa; texto original; status no Delphi (rodada e resultado); versão.

## Anexo F. Lista de documentos para a Plataforma Brasil

Folha de rosto assinada pelo representante da instituição proponente; projeto detalhado (este documento, finalizado); TCLE dos profissionais (Delphi; usabilidade); solicitação de dispensa de TCLE para a auditoria; TCUD; Termo de Anuência Institucional do Hospital do Câncer; declaração de infraestrutura de cada centro; cronograma com início após aprovação; orçamento; currículo Lattes do pesquisador responsável; declaração de conflito de interesse; termo de confidencialidade da equipe; instrumentos (Anexos A, B, C); descrição do fluxo de dados e LGPD.

## Anexo G. Origem das verificações bibliográficas

- Itens `[VERIFICADO]`: PMID e DOI obtidos por consulta programática ao PubMed (E-utilities) em 10/09/2026, a partir de busca por autor, título e periódico, com conferência do registro de metadados.
- Itens `[WEB]`: documentos normativos, diretrizes e capítulos de livro não indexados no PubMed, localizados por busca na internet; os textos oficiais em gov.br e planalto.gov.br não puderam ser abertos a partir do ambiente usado, então artigos, prazos e dispositivos citados desses documentos vieram de fontes secundárias e devem ser conferidos no texto oficial antes da submissão.
- Não localizados: versão brasileira validada do MAUQ; estudo brasileiro publicado que use Delphi especificamente para protocolo de antibioticoterapia empírica hospitalar (o mais próximo é o consenso da ABHH sobre neutropenia febril, `[REF 34]`).
- Títulos entre colchetes na seção 20 são descrições do conteúdo; copiar o título exato do registro PMID ao formatar.
