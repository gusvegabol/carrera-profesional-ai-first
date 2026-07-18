Exploring a New Competency Modeling Process with
Large Language Models
Silin Du, Manqing Xin
SchoolofEconomicsandManagement,TsinghuaUniversity,Beijing,China
dsl21@mails.tsinghua.edu.cn,xmq21@mails.tsinghua.edu.cn
Raymond Jia Wang
Bill-JCTechnology,Wuhan,China
wangjia@bill-jc.com
Last Update: February 16, 2026
Competency modeling is widely used in human resource management to select, develop, and evaluate
talent. However, traditional expert-driven approaches rely heavily on manual analysis of large volumes of
interviewtranscripts,makingthemcostlyandpronetorandomness,ambiguity,andlimitedreproducibility.
This study proposes a new competency modeling process built on large language models (LLMs). Instead
of merely automating isolated steps, we reconstruct the workflow by decomposing expert practices into
structuredcomputationalcomponents.Specifically,weleverageLLMstoextractbehavioralandpsychological
descriptions from raw textual data and map them to predefined competency libraries through embedding-
basedsimilarity.Wefurtherintroducealearnableparameterthatadaptivelyintegratesdifferentinformation
sources, enabling the model to determine the relative importance of behavioral and psychological signals.
Toaddressthelong-standingchallengeofvalidation,wedevelopanofflineevaluationprocedurethatallows
systematicmodelselectionwithoutrequiringadditionallarge-scaledatacollection.Empiricalresultsfroma
real-worldimplementationinasoftwareoutsourcingcompanydemonstratestrongpredictivevalidity,cross-
libraryconsistency,andstructuralrobustness.Overall,ourframeworktransformscompetencymodelingfrom
alargelyqualitativeandexpert-dependentpracticeintoatransparent,data-driven,andevaluableanalytical
process.
Key words: Large Language Models, Competency Modeling, Human Resources Management
1. Introduction
How to select, retain, and cultivate talent is fundamental to maintaining an organization’s compet-
itiveness. To address this challenge, many organizations utilize the notion of competencies as an
integrated framework to understand what enables effective job performance. Competencies are typi-
cally defined as the underlying knowledge, skills, abilities, and other characteristics that distinguish
superior from average performers (Boyatzis 1991, Campion et al. 2011). Building on this idea, com-
petency modeling, which refers to the systematic process of identifying, describing, and organizing
thecompetenciesrequiredforsuccessfulperformanceinaspecificjob,role,ororganizationalcontext,
1
6202
beF
31
]LC.sc[
1v48031.2062:viXra

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
2
Preprint
has become an effective and popular tool (Shippmann et al. 2000). In today’s organizations, com-
petency models form the foundation for various human resource management (HRM) activities and
are an indispensable tool for talent management (Cappelli and Keller 2014). However, along with
the widespread adoption of competency models in the industry, many criticisms and challenges have
emerged, particularly concerning the lack of rigor in the modeling process and the associated costs
(Shippmann et al. 2000, Stevens 2013).
Traditional competency modeling processes often suffer from substantial randomness and ambi-
guity in identifying competencies, resulting in low reproducibility (Shippmann et al. 2000). Much
of this problem comes from the traditional expert-driven workflow. A group of experts needs to
interview participants, read interview transcripts, extract information, and summarize the content
into competency statements. Such qualitative and expert-dependent steps place high demands on
human information processing and make the outcomes highly sensitive to the individual experts
involved. Different groups of experts may produce various results. In addition, competency modeling
ishighlyresource-intensive(Campionetal.2011).Conductinginterviews,analyzinglargeamountsof
transcripts, and reaching expert consensus require substantial time and specialized expertise. Many
organizations cannot easily commit such resources. In practice, attempts to improve model quality,
such as increasing interview coverage, only intensify these demands and further inflate the overall
cost.
Anothermajorlimitationisthatitisextremelydifficulttovalidateacompetencymodelwithinthe
traditional process. Validating a competency model requires collecting additional competency data
fromotheremployeestoverifywhethertheidentifiedcompetenciestrulydistinguishhighandaverage
performers. Organizations may need to conduct more interviews, analyze additional transcripts,
distribute questionnaires, or run assessment center activities. However, all of these methods require
substantial human effort, time, and coordination. For this reason, validation is frequently omitted or
carried out only superficially, leaving many competency models as one-off, unverified products with
uncertain reliability.
The expert-driven process also faces challenges in adaptability. Once a competency model is estab-
lished, it is hard to adjust its structure (e.g., the number of key competencies), limiting the model’s
ability to evolve with changing organizational needs. Although prior research has suggested using
competency libraries1 or establishing advisory panels, the current method for competency modeling
continues to face significant drawbacks.
1Competencylibrariesrefertoalistofcompetenciesavailableforselectionduringthedevelopmentofacompetency
model. These competencies often represent experiences derived from other companies or other projects within the
same company. Utilizing a competency library can simplify and expedite the development of a competency model.
Table 1 shows the structure of a competency library and some examples.

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
3
Preprint
Given these limitations, there is a strong need for a more rigorous, objective, and efficient way to
conduct competency modeling. Many issues above stem directly from the heavy reliance on experts
to read, interpret, and summarize interview transcripts. These limitations highlight the need for a
more scalable and consistent analytical mechanism. The rapid development of large language models
(LLMs) offers a promising technological pathway. Modern LLMs, such as GPT-4 (Achiam et al.
2023), demonstrate exceptional abilities in understanding and generating human language (Zhao
et al. 2023). Empirical studies have shown that LLMs can perform complex and nuanced tasks, such
as identifying non-answers in earnings conference calls (de Kok 2025). These capabilities suggest the
potential of LLMs for automating complex qualitative analyses in competency modeling.
Recent advances have further expanded the context windows of LLMs to more than 100k tokens
(Peng et al. 2023), enabling LLMs to process entire interview transcripts at once. This addresses
one of the major bottlenecks of traditional approaches: the difficulty of systematically analyzing
large volumes of textual data. Furthermore, LLMs can generate outputs rapidly and at relatively
low marginal cost through API services. This reduces the dependence on scarce expert resources and
lowers the barrier for small organizations to carry out competency modeling.
Importantly, LLMs make validation and iterative refinement far more feasible. LLMs can analyze
interview transcripts quickly and consistently, which allows organizations to set aside a portion of
interview data as a test set. After a competency model identifies key competencies that should
separate high and low performers, the LLM can score the test-set interviews on these competencies.
These scores can then be compared directly to the actual performance levels of the individuals
in the test set. This creates a fast, low-cost way to validate whether a competency model truly
works, without requiring experts to repeat large amounts of manual analysis. LLMs thus enable
offline,systematicevaluationofdifferentmodelingchoicesandsupportrapidrefinementoftheoverall
workflow.
Despite these promising opportunities, an open question remains: how should LLMs be integrated
into the competency modeling workflow, and at which stages can they provide the greatest value
whilepreservinginterpretabilityandevaluability?Addressingthisquestionrequiresacarefulredesign
of the competency modeling process to harmonize LLM capabilities with established HR practices.
To this end, we design a new competency modeling process with large language models, namely
CoLLM. The contributions of this paper are threefold.
1. Tothebestofourknowledge,thisisthefirstworktouseLLMstoredesigntheentirecompetency
modeling workflow. We make this core HRM tool more rigorous and efficient, and to enable more
organizations to apply it at a low cost.
2. WeproposeanewLLM-basedcompetencymodelingprocess.First,weusein-contextlearningto
promptLLMstosummarizebehavioralandpsychologicaldescriptionsfromtherawtranscripts.Then

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
4
Preprint
we map the extracted data into the competency library with the embedding models. Additionally,
we design a learnable weight to adaptively integrate the behavioral and psychological data. Finally,
we devise an offline evaluation process for model selection.
3. To verify the effectiveness of the proposed method, we collect real-world data from a software
outsourcing company and conduct extensive experiments and manual comparison.
2. Related Work
2.1. Competency Modeling
The competency model refers to a collection of knowledge, skills, abilities, and other characteristics
necessary for effective performance in a relevant job (Campion et al. 2011). Competency modeling is
an attribute-based form of work analysis that aims to identify the competencies required for specific
roles (Stevens 2013). Competency modeling can be traced back to the 1970s and is often attributed
to the work of McClelland (1973). He argued that traditional intelligence and personality tests were
inadequate in effectively capturing and predicting workplace performance and proposed shifting the
focus to competencies. His approach to comparing high-performing and average-performing individ-
uals deeply influenced the practice of competency modeling. The techniques used in the competency
modeling process significantly overlap with those used in job analysis (Shippmann et al. 2000).
The key differences between competency modeling and job analysis lie in their strategic relevance
and their ability to distinguish between high performance and average performance (Campion et al.
2011).
Howisacompetencymodeldeveloped?BriscoeandHall(1999),throughinterviewswith31leading
North American companies, identified three primary foundations for building competency models:
research-based, strategy-based, and values-based. Campion et al. (2011) systematically outlined the
best practices for competency modeling from a full-cycle perspective, encompassing three topics:
Analyzing Competency Information (Identifying Competencies), Organizing and Presenting Com-
petency Information, and Using Competency Information. Their approach reflects the necessity of
integrating research-based, strategy-based, and values-based approaches in developing competency
models. In practice, a highly valuable tool is the competency library. Over years of practical expe-
rience, the industry has developed several competency libraries that use standardized language to
describe various dimensions of competencies, including skills, knowledge, abilities, etc. Competency
libraries are typically hierarchical, offering terminology at varying levels of granularity to describe
competencies (as illustrated in Table 1). Organizations are strongly advised to select and utilize a
competency library prior to modeling, as this helps establish a comparable conceptual hierarchy and
enhance efficiency (Campion et al. 2011).

| Du et al.: | ExploringaNewCompetencyModelingProcesswithLargeLanguageModels |     |     |     |
| ---------- | ------------------------------------------------------------- | --- | --- | --- |
5
Preprint
| 2.2. Large | Language | Models |     |     |
| ---------- | -------- | ------ | --- | --- |
Recently, both academia and industry have made significant progress in LLMs (Achiam et al. 2023,
Chang et al. 2024). LLMs, distinct from pre-trained language models, are characterized by an enor-
mous number of parameters (usually over 10 billion). As the model size and data size scale up,
LLMs have demonstrated emergent abilities (Wei et al. 2022). The technical evolution of LLMs has
significantly reshaped AI research and expanded their applicability beyond traditional NLP tasks to
complex reasoning, strategic interaction, and structured decision-making settings (Zhao et al. 2023,
| Du and | Liu 2024, | Du and Zhang | 2024, Che | et al. 2024). |
| ------ | --------- | ------------ | --------- | ------------- |
Lowreproducibilityandinefficiencyincompetencymodelingstemfromtherequirementforexperts
to meticulously analyze a large volume of interview transcripts. Fortunately, LLMs exhibit great
abilities to generate summarization, and the quality of LLM-generated summaries is judged on par
withthosewrittenbyhumans(Zhangetal.2024).Meanwhile,thetextembeddingtechniquehasalso
madesignificantadvancementsthankstoLLMs.Neelakantanetal.(2022)initializewordembeddings
with GPT-3 (Brown et al. 2020) and use contrastive training to yield high-quality word representa-
tions. Besides, the context limit of LLMs has been extended to over 100k (Peng et al. 2023), offering
basic conditions to handle extremely long transcripts. Thus, in this paper, we explore a new pro-
cess for competency modeling equipped with LLMs, which first utilizes LLMs to summarize related
descriptions from the raw texts and then uses the text similarity based on the embedding technique
| to construct     | competency | models.    |          |         |
| ---------------- | ---------- | ---------- | -------- | ------- |
| 3. Proposed      |            | Method     |          |         |
| 3.1. Traditional |            | Competency | Modeling | Process |
To begin with, we present a formal definition of competencies as follows.
Definition 1 (Competency). A competency is an underlying characteristic of an individual
that enables effective or superior performance in a job or role, such as knowledge, skills, abilities,
| motives, | or behavioral | tendencies | (McClelland | 1973). |
| -------- | ------------- | ---------- | ----------- | ------ |
Although competencies incorporate elements like skills and abilities, the concept differs in important
ways. Skills refer to learned capabilities to perform specific tasks, and abilities represent innate or
general capacities. Competencies, in contrast, integrate these elements with behavioral patterns and
personalattributes,emphasizinghowindividualsactuallyperforminrealworksituationsratherthan
what they can do in theory. As such, competencies reflect a more holistic and context-dependent
understanding of performance. Based on this, we define the goal of competency modeling as follows.
Definition 2 (Competency Modeling). The goal of competency modeling is to identify,
describe,andorganizethecompetenciesrequiredforeffectiveperformanceinaspecificjob,jobfamily,
| or organizational |     | domain (Shippmann | et al. | 2000). |
| ----------------- | --- | ----------------- | ------ | ------ |

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
6
Preprint
A competency model typically highlights the characteristics that distinguish high performers from
average performers and provides a structured framework for aligning talent selection, development,
performance appraisal, and succession planning. Currently, the tools used to develop competency
models primarily include job analysis interviews, behavioral event interviews (BEI), questionnaires,
and the integration of existing competency libraries. Each method has its advantages and disadvan-
tages,andthechoiceofspecificapplicationprocessesshouldconsidertheorganizationalcontext.Nev-
ertheless, both theory and practice acknowledge the effectiveness and importance of the behavioral
event interview method. In the social sciences, where human subjects are the focus of study, individ-
uals often alter their behavior upon learning they are being observed, attempting to meet perceived
researcher expectations and consequently exhibiting atypical or unintended responses that compro-
mise research outcomes. BEI method effectively mitigates this issue by ensuring the authenticity and
richness of collected data. BEI is a structured interview technique designed to elicit competencies by
exploring specific, real-world situations and detailed behavioral accounts. The BEI process requires
candidatestorecallanddescribespecificcriticalincidentstheyhaveactuallyexperiencedinthepast.
Through systematic probing for concrete details, the method assesses demonstrated competencies,
rather than relying on self-reported claims or idealized self-presentations. BEI is grounded in two
core principles: First, past behavior is considered the most reliable predictor of future performance.
Howanindividualhasactedinsimilarsituationshistoricallystronglyindicateshowtheyarelikelyto
act in the future. Second, the focus is on observable, specific actions within real events, not on stated
attitudes or theoretical opinions. For instance, instead of asking, ”What qualities do you think make
a good leader?” a BEI interviewer would ask, ”Describe a specific challenging situation you faced
while leading a team. What exact steps did you take at the time?” Typically, a classic competency
model development process based on BEI involves:
• Selecting criterion samples: defining high performers and average performers in the target posi-
tion;
• Collecting data: using BEI methods on both groups of samples;
• Analyzing data: performing qualitative analysis on the collected text to extract factors that
differentiate high performers from average performers, and establishing a competency model;
• Validating the model: using methods such as scale development and assessment centers to vali-
date the model’s effectiveness;
• Applying the model: implementing the competency model across various stages of talent acqui-
sition, development, and retention.
The third step (data analysis) is the core of the whole process. In this stage, human experts
meticulously dissect and compare the events gathered from interviews to ultimately identify the
competencies required for the position. Typically, the expert focuses on what the individual did in

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
7
Preprint
the event, as well as their underlying thought process. Although this expert-based data analysis
approach has been used for decades, it still has several significant limitations.
1. Highcostsandlengthymodelingtimelines.Manycompanieslacktheinternalcapabilityto
conductcompetencymodelingand,therefore,oftenneedtoinvestheavilyinhiringexternalconsulting
firms. The expert teams from these firms typically require weeks or even months to analyze BEI
data. As a result, the high cost and time demands limit the scalability of the competency modeling
process across multiple job roles.
2. The Quantity-Quality Paradox.Whileacquiringmoreinterviewdataandemployingdiverse
competencylibrariescantheoreticallyenhancethequalityandrobustnessofthemodel,itsimultane-
ously significantly increases the pressure of information processing and the difficulty of comparative
analysis. Consequently, the traditional modeling process cannot be feasibly improved through intu-
itive methods alone.
3. Low objectivity and reproducibility. Expert-driven modeling heavily relies on domain
expertiseandishighlysubjective.Differentexpertteamsmayproduceinconsistentresults.Moreover,
the data analysis process often involves conflicting opinions that require multiple rounds of group
discussion to reach consensus. Consequently, the resulting models tend to lack reproducibility —
even the same expert team may not arrive at identical results in repeated analyses.
4. Difficulty in validation. Competency models require validation to ensure their accuracy,
typically through scale development and assessment centers. Scale development involves designing
competency questionnaires to evaluate individuals in the same role (excluding those interviewed).
Assessment centers evaluate competencies through written tests, interviews, leaderless group discus-
sions, and situational exercises. Both methods assess the alignment between evaluation results and
the competency model to determine validity. However, they are time-consuming and costly, and due
to a lack of in-house expertise, organizations may skip the validation step altogether.
5. Limited flexibility. Results derived from expert teams are difficult to adjust based on key
settings, such as the choice of competency library, the target level of modeling, or the number of key
competencies.
To this end, we design a new competency modeling process with LLMs, namely CoLLM, aiming
for greater efficiency, improved objectivity and reproducibility, and enhanced flexibility. In addition,
we can apply offline evaluation metrics to our proposed process, which facilitates comparisons across
different designs, thereby complementing existing model validation approaches.
3.2. New Process with LLMs
Figure 1 shows the workflow of our proposed method. Let C={c ,··· ,c } be the set of participants
1 N
inthetargetpositionwithN samplesinthehigh-performancegroupandN samplesintheaverage-
1 2
performance group. Each participant c ∈C has a corresponding text record of the BEI r ∈R. We
i ci

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
8
Preprint
|     | BEI Interview  |     |     |     | Competency  |     | Performance  |     |
| --- | -------------- | --- | --- | --- | ----------- | --- | ------------ | --- |
|     | Text           |     |     |     | Library     |     | Label        |     |
Extraction of Behavioral  Induction – Matching Against  Integration of
and Psychological  Summarization – the Competency  Psychological and
|                  | Descriptions |     | Error Correction |     | Library  |     | Behavioral Data |     |
| ---------------- | ------------ | --- | ---------------- | --- | -------- | --- | --------------- | --- |
| Individual Level |              |     |                  |     |          |     | Group Level     |     |
Competency
Model
Model
Evaluation
|     |     |     | Figure1 | The Workflow | of CoLLM |     |     |     |
| --- | --- | --- | ------- | ------------ | -------- | --- | --- | --- |
divide the set of participants C into the high-performance set C+ ={c+,··· ,c+ } and the average-
1 N1
performance set C− = {c−,··· ,c− }. The competency library is a structured collection of L pre-
|     |     | 1   | N2  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
defined competencies that are considered important for success within an organization, denoted as
M={(m ,T ),··· ,(m ,T )},wherem isthei-thcompetencyitemandT isthetextualdescription
|     | 1 1 | L L | i   |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
of . Given the competency library, a competency model of participant is a set of scores =
| m   |     |     |     |     |     | c   |     | s   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| i   |     |     |     |     |     |     |     | c   |
{sc,sc,...,sc}oneachcompetencyitem.Weomitthesubscriptsorsuperscriptshereafterwhenthere
| 1   | 2 L |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
is no ambiguity.
CoLLMoperatesattwolevels.(1)Individuallevel:Foreachparticipant,weextractbehavioraland
psychological descriptions from their interview transcript, and derive competency scores along these
two dimensions, denoted as sp and sb. (2) Group level: Based on the distribution of competencies in
the high-performance group and the average-performance group, we learn a weight to aggregate
α
the behavioral and psychological scores. This yields group-level competency scores, denoted as S+
and S−.
IndividualLevel. DuringtheBEI,participantsareencouragedtodescribeseveralspecificsituations
(i.e., events) they have encountered in the past, the actions they took, and the outcomes of those
actions. We can easily divide the interview transcript r of c into K distinct segments according to
the different events described by the candidate, i.e., r={r(1),r(2),··· ,r(K)}, where the superscript
denotestheindexoftheevent.Ingeneral,thenumberofsegmentsK islessthan5.Thenweleverage
the in-context learning (ICL) method, first proposed with GPT-3 (Brown et al. 2020), to extract
descriptions related to behaviors and psychology from each segment r(K) through prompting a well-
trained LLM. The prompt template is displayed in Figure 2, including a task definition and a few
| human-written | task | samples as | demonstrations. |     |     |     |     |     |
| ------------- | ---- | ---------- | --------------- | --- | --- | --- | --- | --- |

| Du et al.: | ExploringaNewCompetencyModelingProcesswithLargeLanguageModels |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
9
Preprint
| //Task Description// |     |     |     |     |     |     |     |     |     | //Behavioral Description// |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- |
Assuming you are now a research assistant tasked with conducting a qualitative analysis of
textual materials. These materials were obtained through interviews with practitioners in the  • Actively learn computer knowledge to prepare for
{xxx} industry. Your task is to extract data about the protagonist in the stories, with two  future work
specific requirements.  • Establish connections with banks and financial
| (1) Try your best to extract each text description related to the behaviors(or psychology)  |     |     |     |     |     |     |     |     |     | institutions |     |     |     |     |
| ------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
of the protagonist, summarizing each piece of behavioral (or psychological) description in a  • Emphasize compliance, ensuring that team members
phrase or a sentence;  adhere to legal and regulatory requirements.
| (2) After each extracted behavioral (or psychological) data, point out the original text  |     |     |     |     |     |     |     |     |     | • …… |     |     |     |     |
| ----------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
reference.  Note that there should be no repetition.
//Demonstration//
Here are some examples related to behavioral (or psychological) descriptions
• ***********************
• ***********************
……
| //Raw Text of Segment 𝒓(𝒊)// |     |     |     |     |     |     |     |     |     | //Psychological Description// |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
……
• Maintain an upbeat and positive mindset in the face
of difficulties.
//Format Instruction//
Please response in JSON format. Here are the format requirements for the output:  • Strive for a psychological trait of high efficiency and
cost-effectiveness.
{
summary of behavioral (or psychological) data 1: original text reference, • Engage in self-reflection and introspection about
one’s abilities and actions.
summary of behavioral (or psychological) data 2: original text reference,
| }   |     |     |     |     |     |     |     |     |     | • …… |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
Figure2 Prompt Template for Extraction of Behavioral and Psychological Descriptions
To avoid omissions, we employ three different temperature parameters2 to obtain multiple results.
|     |     |     | (cid:16) |     | (cid:17) |     | (cid:16) |     | (cid:17) |     |     |     |     |     |
| --- | --- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- |
o(j) =ICL r(j),τ ,t ,o(j) =ICL r(j),τ ,t ,τ ∈{τ ,τ ,τ },j=1,···K (1)
|     |     |      |     | i   | b    |     |     | i p | i   | 1   | 2 3 |     |     |     |
| --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | b,τi |     |     | p,τi |     |     |     |     |     |     |     |     |     |
where t and t are prompt templates for behavioral and psychological analysis respectively, τ is
|     | b   | p   |     |     |     |     |     |     |     |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the temperature parameter, and o(j) , are extracted behavioral and psychological descriptions
o(j)
|     |     |     |     |     | b,τi | p,τi |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
in the segment r(j). In this step, we control the generation seed of the LLM to ensure reproducibility.
Behavioral and psychological descriptions are at the core of competency modeling, and any errors or
omissionscouldpotentiallyaffecttheoutcomes.WeintroduceanLLM-basedreviewsteptointegrate
results from different temperatures while also filtering out incorrect descriptions. The prompt tem-
platesinthisstepareroughlythesameasthoseinFigure2,withaslightlydifferenttaskdescription.
|     |                 |     |     | (cid:16) |           |        | (cid:17) |                 |     |     | (cid:16)   |      | (cid:17) |     |
| --- | --------------- | --- | --- | -------- | --------- | ------ | -------- | --------------- | --- | --- | ---------- | ---- | -------- | --- |
|     | o˜(j)=LLMReview |     |     | o(j)     | ,o(j)     | , o(j) | ,        | o˜(j)=LLMReview |     |     | o(j) ,o(j) | ,    | o(j)     |     |
|     |                 | b   |     |          | b,τ1 b,τ2 | b,τ3   |          | p               |     |     | p,τ1       | p,τ2 | p,τ3     |     |
After that, we transform the behavioral and psychological data of each event to document embed-
dings, i.e.,
|     |     |     | o =emb(o˜(1),o˜(2),··· |     |     | ,o˜(K)),o |     | =emb(o˜(1),o˜(2),··· |     |     | ,o˜(K)) |     |     |     |
| --- | --- | --- | ---------------------- | --- | --- | --------- | --- | -------------------- | --- | --- | ------- | --- | --- | --- |
|     |     |     | b                      | b   | b   |           | b   | p                    | p   | p   | p       |     |     |     |
Similarly, we can represent each competency item of the library in the same latent semantic space
m
i
by mapping the textual description to an embedding vector, i.e., =emb(T ),i=1,··· ,L. Then
|     |     |     |     |     | T   |     |     |     |     |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | i   |     |     |     |     |     | i   | i   |     |     |
we calculate two scores on each competence item m through the behavioral and psychological data.
i
tTo
|     |     | sb=cos<t |     |     | >=  | b    | sp=cos<t |     |     |     | i=1,··· |     |     | (2) |
| --- | --- | -------- | --- | --- | --- | ---- | -------- | --- | --- | --- | ------- | --- | --- | --- |
|     |     |          |     | ,o  |     | i    | ,        |     | ,o  | >,  |         | ,L  |     |     |
|     |     | i        |     | i b | |t  | |·|o | | i      |     | i   | p   |         |     |     |     |
i b
2ThetemperatureparameterinLLMsisahyperparameterthatcontrolstherandomnessorcreativityofthegenerated
text. When the temperature is above 1, the model will generate more diverse and creative text. A temperature of 0
| is equivalent | to greedy |     | decoding, | leading | to very | repetitive |     | and deterministic |     | text. |     |     |     |     |
| ------------- | --------- | --- | --------- | ------- | ------- | ---------- | --- | ----------------- | --- | ----- | --- | --- | --- | --- |

|     |     | Du et al.: | ExploringaNewCompetencyModelingProcesswithLargeLanguageModels |     |     |     |     |
| --- | --- | ---------- | ------------------------------------------------------------- | --- | --- | --- | --- |
10
Preprint
Given sb=[sb, ,sb] and sp=[sp, ,sp] for each participant, we average scores
| Group Level. |     | ··· |     | ··· |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
|              |     | 1 L |     | 1 L |     |     |     |
ofindividualswithinthehigh-performanceandaverage-performancegroupstogetgroup-levelresults,
i.e., Sb,+,Sp,+ and Sb,−,Sp,−. To obtain the final competency model, we need to combine the results
derived from behavioral and psychological data. One straightforward method is to simply add them
together, assuming that psychological and behavioral data play the same role in the competency
model. However, for different organizations, or even different positions within the same organization,
the weight of psychological and behavioral data in the competency model may not be the same. For
this reason, we introduce a learnable weight, α, to integrate group-level behavioral and psychological
results.
|     |     | S+=Sb++α·Sp,+, |     | S−=Sb,−+α·Sp,− |     |     | (3) |
| --- | --- | -------------- | --- | -------------- | --- | --- | --- |
Theoretically, a good should result in a significant difference in competency scores between the
α
high-performance group and the average-performance group. We design a loss function based on
the triplet loss used in face recognition (Schroff et al. 2015) to learn α. Each training sample is a
triplet (c,c′,c′′) consisting of a randomly selected participant c∈C, an individual c′ from the same
performance group as c, and a participant from the other group. The similarity of competency
c′′
scores weighted by within the same performance group is desired to be higher than that between
α
| different groups. | Therefore, | we define | the following | loss function. |     |     |     |
| ----------------- | ---------- | --------- | ------------- | -------------- | --- | --- | --- |
l(c,c′,c′′;α)=cos<sb+αsp, sb +αsp > − cos<sb+αsp, sb +αsp > (4)
|     |     | c   | c c′′ | c′′ | c c | c′ c′ |     |
| --- | --- | --- | ----- | --- | --- | ----- | --- |
Subsequently, we leverage stochastic gradient descent to optimize the loss function and get the
optimizedweightingparameterα.Weobtainthefinalcompetencymodelsoftwoperformancegroups
by plugging α into Eq. (3). Now we can rank each item in the competency library based on the
scores difference between the two performance groups, i.e., S+−S−, thereby identifying the critical
competencies.
| 3.3. Offline | Evaluation |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- |
Existing methods for validating competency models typically require large-scale competency assess-
ments of other individuals in the same role (e.g., through questionnaires or assessment centers). We
refer to these methods relying on the collection of new data as online evaluation methods, which
often entail high costs and long assessment cycles. As a result, organizations may skip rigorous val-
idation steps in practice. In contrast, this subsection focuses on offline evaluation methods without
| the collection | of new data. |     |     |     |     |     |     |
| -------------- | ------------ | --- | --- | --- | --- | --- | --- |
First, we randomly select N participants (around 20%–25%) from C as a test set C , with
|     |     | test |     |     |     | test |     |
| --- | --- | ---- | --- | --- | --- | ---- | --- |
the remaining participants forming the training set. On the training set, we learn α to compute the
competency scores for the two performance groups, denoted as S+ and S− . Next, we identify
|     |     |     |     |     | train | train |     |
| --- | --- | --- | --- | --- | ----- | ----- | --- |

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
11
Preprint
the top-Q competency items with the largest differences in S+ −S− , and treat them as key
train train
competencies.WethenapplythesameprocessandthelearnedαtoC tocomputeeachparticipant’s
test
average score across the Q key competencies. Based on these average scores, we rank all participants
in C , resulting in a ranking Y =(y ,y ,...,y ), where y ∈C is the participant ranked at i-th
| test |     |     | 1   | 2 Ntest |     | i test |     |
| ---- | --- | --- | --- | ------- | --- | ------ | --- |
position in Y. Similarly, we rank the same participants based on their actual performance to obtain
Z =(z ,z ,...,z ),z ∈C . We use Spearman’s rank correlation (Spearman 1904) to quantify
| 1 2 | Ntest i | test |     |     |     |     |     |
| --- | ------- | ---- | --- | --- | --- | --- | --- |
thesimilaritybetweenY andZ,therebyreflectingtheextenttowhichthekeycompetenciesextracted
| from the training | set align | with | the actual | performance. |          |          |     |
| ----------------- | --------- | ---- | ---------- | ------------ | -------- | -------- | --- |
|                   |           |      | 6P         | (rank        | (c)−rank | (c))2    |     |
|                   |           | ρ=1− |            | c∈Ctest      | Y        | Z        | (5) |
|                   |           |      |            |              | (cid:16) | (cid:17) |     |
|                   |           |      |            | N            | N        | 2−1      |     |
|                   |           |      |            | test         | test     |          |     |
where rank (c) and rank (c) denote the rank of in and Z, respectively.
|     |     |     |     |     | c Y |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Y Z
Inpractice,afullrankingofparticipantperformancemightbeunavailable;instead,eachcandidate
istypicallyassignedabinaryperformancelabel.Inthissetting,wetreattheaveragekey-competency
score as a continuous prediction and use the Area Under the ROC Curve (AUC) as an additional
| evaluation metric. |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
4. Experiments
In this section, we conduct extensive experiments to answer the following questions.
• Can our CoLLM framework produce a coherent and interpretable competency model for a given
target role?
We begin by presenting a full modeling example to illustrate how behavioral and psychological
evidence is transformed into competency scores and how key competencies emerge.
| • How to determine | the | number | of key | competencies? |     |     |     |
| ------------------ | --- | ------ | ------ | ------------- | --- | --- | --- |
We evaluate competency models constructed under different numbers of key competencies using
the evaluation method described in Section 3.3, and identify the number that yields the best overall
performance.
• How robust is the modeling process when we replace the underlying LLM or compare against
| human expert | coders? |     |     |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- | --- | --- |
We evaluate the generalizability of our framework by changing the backend LLMs. Besides, we
invite human experts to manually extract behavioral and psychological descriptions from interview
transcripts. This allows us to assess the reliability of substituting human coding with LLM-based
extraction.
• Are the identified key competencies consistent across different competency libraries?
We replace the target competency framework with alternative libraries and replicate the full
pipeline.

|     |     |     | Du  | et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
12
Preprint
| 4.1. Data | Collection |     | and Settings |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
ToevaluatetheCoLLMprocess,wecollaboratewithacompanyinthesoftwareoutsourcingindustry.
Wechoosetheteamleaders(TLs)asthetargetpositionincompetencymodeling.TheseTLsserveas
the on-site leaders for outsourced employees at the client company, responsible for coordinating task
delivery, team development, and communication between the client and the outsourcing team. There
are hundreds of TLs in this company and we conduct behavioral event interviews (BEI) with 40 TLs
in a month, with 18 in the high-performance group and 22 in the average-performance group. The
criterion for grouping is the performance of each manager in the previous 3 months. Each interview
lasts about 2 hours, and all participants mention at least three events that have played a significant
| role in their | careers. |     |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We use the “67 Lominger Competencies (Fifth Edition)” (Lombardo and Eichinger 2010) as the
competency library, which has already been widely adopted by the company. The library contains
three levels with 67 competencies at the third level, 20 clusters at the second level, and 6 factors at
the top level. Some examples of the library are displayed in Table 1. Each cluster and competency
has a short text description, i.e., T in our process. We focus on the 20 clusters at the second level
i
as the modeling targets. Due to copyright restrictions, we do not provide a detailed discussion of the
specific meanings of these clusters. However, Appendix A lists the names and brief descriptions of
all 20 clusters. Interested readers may refer to Lombardo and Eichinger (2010) for a comprehensive
explanation.Wefollowthedefaultnumberinginthecompetencylibrary,using“A”to“T”torepresent
the 20 clusters of competencies. Consistent with the traditional practice, we first set the number of
key competencies to one-third of the total competencies, which yields Q=7 in our context. We then
further explore how to determine the optimal value of in Section 4.3. We select Qwen2.5-Max
Q
(Yang et al. 2024) as the primary LLM in the CoLLM process with τ =0,τ =0.5, and τ =1. The
|             |     |        |                |                  |            |         |          | 1        | 2   | 3   |
| ----------- | --- | ------ | -------------- | ---------------- | ---------- | ------- | -------- | -------- | --- | --- |
| random seed | is  | set to | 2025 to ensure | reproducibility. |            |         |          |          |     |     |
|             |     | Table1 | Structure      | of the           | Competency | Library | and Some | Examples |     |     |
Top-level (Factors) Second-level (Clusters) Third-level (Competencies)
|     |     |     | A: Understanding | the         | Business      |     | 5. Business |          | Acumen      |               |
| --- | --- | --- | ---------------- | ----------- | ------------- | --- | ----------- | -------- | ----------- | ------------- |
|     |     |     | • Is familiar    | with        | the business; |     | • Is        | familiar | with        | the business; |
|     |     |     | • Master         | the key     | technologies  |     | • Master    |          | the key     | technologies  |
|     |     |     | and skills       | required in | work;         |     | and skills  | required | in          | work;         |
|     |     |     | • Knows          | operational | programs      |     | • Knows     |          | operational | programs      |
I:
| Strategy | Skills |     |                   |            |         |     |                 |         |            |             |
| -------- | ------ | --- | ----------------- | ---------- | ------- | --- | --------------- | ------- | ---------- | ----------- |
|          |        |     | and their general | operation; |         |     | and their       | general | operation; |             |
|          |        |     | • Can learn       | new        | methods | and | • Is            | able    | to learn   | new methods |
|          |        |     | techniques;       |            |         |     | and techniques; |         |            |             |
24.
|     |     |     |     |     |     |     | Functional/Technical |     |          | Skills |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | -------- | ------ |
|     |     |     |     |     |     |     | 61. Technical        |     | Learning |        |

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
13
Preprint
4.2. Competency Modeling Results
In this subsection, all 40 participants are included for modeling. Figure 3 shows the sb and sp
of a selected participant. The top-7 clusters of competencies derived from his behavioral data are
L/A/G/F/B/H/T, and those obtained from his psychological data are B/G/T/L/H/F/P. After get-
ting sb and sp for each participant, we construct 400 triplets from our training set and use AdamW
(Loshchilov and Hutter 2018) to optimize Eq. (4) for 2000 epochs. Figure 4 illustrates the variation
of the loss during the training process. The optimized α is 12.23, indicating that for the TLs of this
company, the psychological data in their competencies is much more important than the behavioral
data. Traditional processes of competency modeling are not capable of analyzing or revealing this
finding.
Behavioral Psychological
A B C D E F G H I J K L M N O P Q R S T A B C D E F G H I J K L M N O P Q R S T
(a) (b)
Figure3 Scores on Each Competence Item Derived from Behavioral (Left) and Psychological (Right)
Descriptions of a Participant
Plugging α=12.23 into Eq. (3) yields the group-level results, shown in Figure 5. We summarize
that the seven most critical clusters of competencies are R/I/P/N/S/D/L. This suggests that for the
branch managers of this company, the following seven capabilities are very important: acting with
honorandcharacter,makingtoughpeoplecalls,managingdiverserelationships,relatingskills,Being
Open and Receptive, keeping on point, and communicating effectively.
Besides, we invite two experts to analyze the participant presented in Figure 3. They rigorously
follow the traditional process to code the BEI data and determine which clusters of competencies the
participant aligns with. The top-5 competencies identified by experts are B/H/L/P/T. We leverage
the optimized α to integrate sb and sp of this participant, and the seven most significant clusters
are B/G/L/T/H/F/P, containing all competencies found by human experts. This demonstrates the
validity and rationality of using LLMs for competency analysis.

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
14
Preprint
Loss
-0.024
-0.026
-0.028
-0.030
-0.032
-0.034
-0.036
0 250 500 750 1000 1250 1500 1750 2000
Figure4 Loss for Each Epoch
0
A B C D E F G H I J K L M N O P Q R S T
Figure5 Differences in Scores between the High-performance Group and the Average-performance Group
4.3. Determine the Number of Key Competencies
In practice, the number of key competencies Q is typically selected within a relatively narrow range,
oftenbetween5and10.Intraditionalexpert-drivencompetencymodeling,thischoicelargelydepends
on the collective judgment and experience of the expert team. While such an approach benefits from
domain expertise, it suffers from several limitations. First, the selection of Q is often subjective and
lacks a transparent quantitative justification. Second, different expert teams may arrive at different

| Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels |     |     |     |     |     |     |
| ------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
15
Preprint
values of Q, leading to limited reproducibility. Third, without systematic validation, the chosen
Q
may not optimally distinguish high performers from average performers.
In contrast, our LLM-based workflow enables rapid and repeated construction of competency
models under different configurations. Leveraging the offline evaluation framework introduced in
Section 3.3, we can systematically vary Q within the range of 5 to 10 and identify the value that
yieldsthebestpredictiveperformance.Thisdata-drivenproceduretransformstheselectionofQfrom
a heuristic decision into an empirically grounded model selection problem.
Specifically, we use a four-fold cross-validation procedure. The dataset is evenly divided into four
subsets.Ineachround,onesubsetservesasthetestset,andtheremainingthreeareusedtobuildthe
competency model by the CoLLM pipeline. We then select the top-Q competencies with the largest
performance-group differences and compute each participant’s average score on these competencies
in the test set. The resulting ranking is compared with their actual performance. The evaluation
metric in Section 3.3 is calculated for each fold, and the four results are averaged.
This procedure allows us to examine how different values of influence the model’s ability to
Q
distinguish performance levels and to identify the optimal number of key competencies.
Spearman's Rank Correlation: mean with ~95% CI band AUC: mean with ~95% CI band
| 0.5 |     |     |     | 0.8 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
noitalerroC knaR s'namraepS
0.4
0.7
0.3
| 0.2 |     |     |     | CUA |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0.6
0.1
| 0.0 |     |     |     | 0.5 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
-0.1
0.4
-0.2
|     | 5 6                        | 7 8     | 9 10               | 5 6                    | 7 8                        | 9 10 |
| --- | -------------------------- | ------- | ------------------ | ---------------------- | -------------------------- | ---- |
|     | Number of Key Competencies |         |                    |                        | Number of Key Competencies |      |
|     |                            | (a)     |                    |                        | (b)                        |      |
|     |                            | Figure6 | Offline Evaluation | Results with Different | Q                          |      |
Figure 6 presents the offline evaluation results. As shown in the figure, the competency model
generated by CoLLM achieves the best performance when Q=9. On the test set, the AUC between
the ranking based on key competencies and the actual performance ranking exceeds 0.7, and the
Spearman rank correlation coefficient is greater than 0.3. These results indicate that the selected key
competencies exhibit strong discriminative ability and a meaningful positive association with actual
| performance, | suggesting | good predictive | validity | of the model. |     |     |
| ------------ | ---------- | --------------- | -------- | ------------- | --- | --- |
Based on the results above, we set Q=9 and use the full sample to construct the final competency
model. Compared with the results reported in Subsection 4.2, two additional clusters, C and F, are

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
16
Preprint
includedamongthekeycompetencies.Thesecorrespondtocreatingthenewanddifferentandgetting
| work | done through |     | others, respectively. |          |     |     |     |     |     |
| ---- | ------------ | --- | --------------------- | -------- | --- | --- | --- | --- | --- |
| 4.4. | Ablation     | and | Robustness            | Analysis |     |     |     |     |     |
Using the same four-fold cross-validation procedure described in Subsection 4.3, we compare the
performance of CoLLM under different backend LLMs. Furthermore, we conduct additional analyses
by replacing or removing specific modules within CoLLM. The following variants are considered for
comparison:
1. CoLLM-GLM and CoLLM-Doubao: Variants of the CoLLM framework using different LLMs,
| specifically |     | GLM-4-plus | and Doubao-1.5-pro, |     | respectively. |     |     |     |     |
| ------------ | --- | ---------- | ------------------- | --- | ------------- | --- | --- | --- | --- |
2. CoLLM−: A simplified version of the CoLLM where we remove the step of learning α and set
| α=1, | treating | behavioral | and psychological |     | data as | equally important. |     |     |     |
| ---- | -------- | ---------- | ----------------- | --- | ------- | ------------------ | --- | --- | --- |
3. CoLLM-expert: three competency modeling experts manually extract behavioral and psycho-
logical descriptions from the interview transcripts, while all other steps remain unchanged.
|     |              |     | Table2  | Evaluation | Results | of Different | Variants         |             |      |
| --- | ------------ | --- | ------- | ---------- | ------- | ------------ | ---------------- | ----------- | ---- |
|     | Method       |     | Optimal |            | AUC     |              | Key Competencies |             |      |
|     |              |     |         | Q          |         | ρ            |                  |             |      |
|     | CoLLM        |     | 9       |            | 0.715   | 0.350        | R, I, P,         | N, S, D, L, | C, F |
|     | CoLLM-GLM    |     | 8       |            | 0.707   | 0.332        | R, P, I,         | C, D, N, L, | S    |
|     | CoLLM-Doubao |     | 8       |            | 0.711   | 0.3467       | P, I, D,         | C, R, L, S, | F    |
|     | CoLLM−       |     | 7       |            | 0.6571  | 0.267        | I, P, R,         | N, S, M, T  |      |
|     | CoLLM-expert |     | 6       |            | 0.721   | 0.351        | N, R, S,         | P, T, F     |      |
Table 2 shows the evaluation results. First, CoLLM achieves strong and stable performance across
different backend LLMs, with only slight fluctuations in AUC and ρ when replacing the underlying
model.ThissuggeststhattheoverallframeworkisrobusttothechoiceofLLM.Second,removingthe
weight-learning step (CoLLM−) leads to a noticeable performance drop, indicating that dynamically
learning the relative importance of behavioral and psychological data is critical for model effective-
ness. Third, the CoLLM-expert variant achieves performance comparable to the original CoLLM,
and even slightly higher AUC, suggesting that LLM-based extraction can effectively approximate
| expert-level |     | coding. |     |     |     |     |     |     |     |
| ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Beyond performance metrics, the identified key competencies are also highly consistent across
variants. Most backend LLMs produce overlapping sets of competencies, with core clusters such as
R, P, N, S, and L appearing repeatedly. Importantly, most of the competencies identified by CoLLM-
expert are also captured by CoLLM , indicating strong structural agreement between LLM-based
| extraction | and | human | coding. |     |     |     |     |     |     |
| ---------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- |
Overall, the results demonstrate both the robustness of the framework and the importance of its
| key | design | components. |     |     |     |     |     |     |     |
| --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
17
Preprint
| 4.5. Cross-library | Robustness |     |     |     |     |     |
| ------------------ | ---------- | --- | --- | --- | --- | --- |
Traditionalexpert-drivencompetencymodelingneedstofixthetargetlibraryatthebeginning.Once
the process begins, changing the framework requires much extra work, such as re-coding interview
data and re-aggregating results. In contrast, the competency library functions as a plug-and-play
module in the CoLLM framework. Our pipeline allows the target library to be replaced without
altering the upstream extraction and scoring procedures, thereby providing significantly greater flex-
ibility.
In this subsection, we evaluate the robustness of our framework by replacing the original com-
petency library with alternative libraries. First, we adopt an alternative competency framework
developedbyKornFerry.Thislibraryissingle-layeredandconsistsof38competenciesorganizedinto
four dimensions: Thinking, Results, People, and Self. Table 3 presents several illustrative examples.
The 38 competency items in the Kon Ferry library are indexed from 1 to 38.
|        | Table3 Some | Examples        | of the Alternative | Competency        | Library           |          |
| ------ | ----------- | --------------- | ------------------ | ----------------- | ----------------- | -------- |
| Number | Dimension   | Competency      |                    | Definition        |                   |          |
|        |             |                 |                    | Applies knowledge | of business       | and      |
| 1      | Thinking    | Business        | Insight            | the marketplace   | to advance        | the      |
|        |             |                 |                    | organization’s    | goals.            |          |
|        |             |                 |                    | Takes on          | new opportunities | and      |
|        |             |                 |                    | tough challenges  | with a            | sense of |
| 11     | Results     | Action-Oriented |                    |                   |                   |          |
|        |             |                 |                    | urgency,          | high energy, and  |          |
enthusiasm.
In addition, we conduct modeling using the third level of the 67 Lominger Competencies, treating
all 67 individual competency items as modeling targets instead of the 20 second-level clusters. The
67 competency items are indexed from 1 to 67. For simplification, we refer to the two levels of the
67 Lominger Competencies as the Longmier second level and the Longmier third level, respectively.
Forbothalternativelibraries,wecompareCoLLMandCoLLM-expert.Wefirstfollowthefour-fold
cross-validation procedure described in Section 4.3 to obtain evaluation results and determine the
optimal value of Q. We then use the full sample to construct the final competency model under each
library.
Table 4 reports the evaluation results across different competency libraries. First, CoLLM achieves
consistently strong performance under all three libraries. The AUC remains around 0.69–0.73 and ρ
around 0.29–0.35, indicating stable discriminative ability across alternative competency structures.
In contrast, CoLLM-expert shows substantial performance variation. While it performs comparably
toCoLLMundertheLongmiersecondlevel(AUC=0.721,ρ=0.351),itsperformancedropssharply

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
18
Preprint
|        |     | Table4          | Results of Different | Competency | Libraries |                  |             |      |
| ------ | --- | --------------- | -------------------- | ---------- | --------- | ---------------- | ----------- | ---- |
| Method |     | Library         |                      | AUC        |           | Key Competencies |             |      |
|        |     |                 | Q                    |            | ρ         |                  |             |      |
|        |     | Longmier Second |                      |            |           |                  |             |      |
|        |     |                 | 9                    | 0.715      | 0.350     | R, I, P,         | N, S, D, L, | C, F |
Level
CoLLM
|     |     | Longmier Third |     |       |       | 37, 33, | 25, 3, 15, 41, | 67, |
| --- | --- | -------------- | --- | ----- | ----- | ------- | -------------- | --- |
|     |     |                | 8   | 0.691 | 0.293 |         |                |     |
|     |     | Level          |     |       |       | 51      |                |     |
|     |     |                |     |       |       | 20, 29, | 2, 19, 21, 13, | 26, |
|     |     | Kon Ferry      | 9   | 0.725 | 0.349 |         |                |     |
22, 24
|        |     | Longmier Second |     |       |        |            |             |     |
| ------ | --- | --------------- | --- | ----- | ------ | ---------- | ----------- | --- |
|        |     |                 | 6   | 0.721 | 0.351  | N, R, S,   | P, T, F     |     |
| CoLLM- |     | Level           |     |       |        |            |             |     |
| expert |     | Longmier Third  |     |       |        | 25, 3, 37, | 23, 26, 60, | 44, |
|        |     |                 | 9   | 0.502 | −0.017 |            |             |     |
|        |     | Level           |     |       |        | 21, 29     |             |     |
|        |     | Kon Ferry       | 5   | 0.501 | 0.001  | 26, 20,    | 23, 24, 22  |     |
under the Longmier third level and the Kon Ferry library (AUC 0.50 and close to 0). This
|     |     |     |     |     | ≈   |     | ρ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
suggeststhatexpert-basedextractionismoresensitivetochangesinlibrarygranularityandstructure,
whereas CoLLM generalizes more robustly across different competency frameworks.
Second, the two methods exhibit high structural consistency within the Longmier library. For
example,thecompetenciesidentifiedbyCoLLMatthethirdlevel(33,25,3,15,41,67)correspondto
clustersS,I,N,P,S,andLatthesecondlevel,whicharealsoincludedinthesecond-levelresults.This
hierarchical alignment indicates that the extracted competencies are conceptually coherent across
levels. Furthermore, Table 4 also reveals cross-library consistency. For instance, CoLLM identifies
clusters I (Making Tough People Calls), L (Communicating Effectively), and F (Getting Work Done
Through Others) at the Longmier second level. These clusters correspond closely to competency
items 22 (Attracts Top Talent), 26 (Communicates Effectively), and 13 (Directs Work) in the Korn
Ferry library. This cross-library alignment suggests that CoLLM captures underlying competency
constructs rather than artifacts specific to a particular taxonomy, thereby demonstrating conceptual
| robustness | beyond | any single predefined | competency | structure. |     |     |     |     |
| ---------- | ------ | --------------------- | ---------- | ---------- | --- | --- | --- | --- |
Third, in the Kon Ferry library, the nine key competencies identified by CoLLM cover four out
of the five competencies identified by CoLLM-expert, further confirming that the extraction process
traditionally performed by human experts can be effectively replicated by LLMs.
These results highlight the adaptability of the proposed framework and its ability to preserve
| conceptual     | consistency | under varying | competency | taxonomies. |     |     |     |     |
| -------------- | ----------- | ------------- | ---------- | ----------- | --- | --- | --- | --- |
| 5. Conclusions |             | and Future    | Directions |             |     |     |     |     |
Competency modeling has long been criticized for its limited rigor, high implementation costs, and
heavy reliance on expert judgment. In this study, we propose a novel LLM-enhanced workflow that
systematically restructures the traditional competency modeling process. By integrating LLMs into

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
19
Preprint
competencyextraction,scoring,andmodelselection,ourframeworktransformswhathashistorically
been a largely subjective procedure into a more transparent, data-driven, and reproducible process.
Through extensive offline evaluations, we demonstrate that the proposed CoLLM framework
achieves strong predictive validity, robust performance across alternative competency libraries, and
high structural consistency across different levels of granularity. The framework not only approxi-
mates expert-level extraction but also introduces a fully data-driven optimization mechanism that
allows the entire modeling process to determine the most suitable configuration, such as the opti-
mal number of key competencies. These features significantly enhance modeling efficiency, reduce
subjective bias, and substantially lower implementation costs. As a result, competency modeling
becomes more scalable and accessible, particularly for small and medium-sized enterprises that may
lack dedicated expert teams.
This study opens several avenues for future research. First, while our validation relies on cross-
sectional performance differences, future work could incorporate longitudinal or lagged performance
data to further examine the causal and predictive validity of the constructed competency models.
Second, expanding the framework to larger and more diverse organizational samples would allow
researchers to test its generalizability across industries and cultural contexts. Finally, investigating
theinterpretabilityandgovernanceimplicationsofLLM-assistedcompetencymodelingrepresentsan
important direction, especially as organizations increasingly rely on AI-supported decision systems.
References
Achiam J, Adler S, Agarwal S, Ahmad L, Akkaya I, Aleman FL, Almeida D, Altenschmidt J, Altman S,
Anadkat S, et al. (2023) Gpt-4 technical report. arXiv preprint arXiv:2303.08774 .
Boyatzis RE (1991) The competent manager: A model for effective performance (John Wiley & Sons).
Briscoe JP, Hall DT (1999) Grooming and picking leaders using competency frameworks: Do they work? an
alternative approach and new guidelines for practice. Organizational dynamics 37–37.
Brown TB, Mann B, Ryder N, Subbiah M, Kaplan JD, Dhariwal P, Neelakantan A, Shyam P, Sastry G,
Askell A, Agarwal S, Herbert-Voss A, Krueger G, Henighan T, Child R, Ramesh A, Ziegler DM, Wu
J, Winter C, Hesse C, Chen M, Sigler E, Litwin M, Gray S, Chess B, Clark J, Berner C, McCandlish
S, Radford A, Sutskever I, Amodei D (2020) Language models are few-shot learners. Advances in
Neural Information Processing Systems, volume 33, 1877–1901 (Curran Associates, Inc.), URL https:
//arxiv.org/abs/2005.14165.
Campion MA, Fink AA, Ruggeberg BJ, Carr L, Phillips GM, Odman RB (2011) Doing competencies well:
Best practices in competency modeling. Personnel psychology 64(1):225–262.
CappelliP,KellerJ(2014)Talentmanagement:Conceptualapproachesandpracticalchallenges.Annu. Rev.
Organ. Psychol. Organ. Behav. 1(1):305–331.

|     |     |     |     | Du et | al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels |     |     |     |     |
| --- | --- | --- | --- | ----- | ------------------------------------------------------------------ | --- | --- | --- | --- |
20
Preprint
Chang Y, Wang X, Wang J, Wu Y, Yang L, Zhu K, Chen H, Yi X, Wang C, Wang Y, et al. (2024) A
surveyonevaluationoflargelanguagemodels.ACM transactions on intelligent systems and technology
15(3):1–45.
CheS,MaoM,LiuH(2024)Newcommunitycold-startrecommendation:Anovellargelanguagemodel-based
method.Proceedings 2024)(Association
|     |     |     | of the | International |     | Conference | on  | Information | Systems (ICIS |
| --- | --- | --- | ------ | ------------- | --- | ---------- | --- | ----------- | ------------- |
for Information Systems), URL https://aisel.aisnet.org/icis2024/data_soc/data_soc/6.
deKokT(2025)Chatgptfortextualanalysis?howtousegenerativellmsinaccountingresearch.Management
.
Science
Du S, Liu H (2024) Large language models for listwise talent recommendation. Proceedings of the Interna-
tional Conference on Information Systems (ICIS 2024) (Association for Information Systems), URL
https://aisel.aisnet.org/icis2024/aiinbus/aiinbus/9.
Du S, Zhang X (2024) Helmsman of the masses? evaluate the opinion leadership of large language models in
| the | werewolf | game. |       |            |     |          | Modeling, | URL |                               |
| --- | -------- | ----- | ----- | ---------- | --- | -------- | --------- | --- | ----------------------------- |
|     |          |       | First | Conference | on  | Language |           |     | https://openreview.net/forum? |
id=xMt9kCv5YR.
Lombardo MM, Eichinger RW (2010) The Career Architect Development Planner: A systematic approach
to development including 103 research-based and experience-tested development plans and coaching tips
| (Korn/Ferry |           | International), |        | 5 edition,    | ISBN  | 978-1933578224. |     |          |     |
| ----------- | --------- | --------------- | ------ | ------------- | ----- | --------------- | --- | -------- | --- |
| Loshchilov  | I, Hutter | F               | (2018) | Fixing weight | decay | regularization  |     | in adam. |     |
arXiv preprint arXiv:1711.05101
| URL | https://arxiv.org/abs/1711.05101. |     |     |     |     |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
McClellandDC(1973)Testingforcompetenceratherthanforintelligence.AmericanPsychologist 28(1):1–14,
| URL | http://dx.doi.org/10.1037/h0034092. |     |     |     |     |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Neelakantan A, Xu T, Puri R, Radford A, Han JM, Tworek J, Yuan Q, Tezak N, Kim JW, Hallacy C
(2022) Text and code embeddings by contrastive pre-training. arXiv preprint arXiv:2201.10005 URL
https://arxiv.org/abs/2201.10005.
Peng B, Quesnelle J, Fan H, Shippole E (2023) Yarn: Efficient context window extension of large language
models.ProceedingsoftheTwelfthInternationalConferenceonLearningRepresentations(ICLR),URL
https://openreview.net/forum?id=Ff9R2S0gwr.
SchroffF,KalenichenkoD,PhilbinJ(2015)Facenet:Aunifiedembeddingforfacerecognitionandclustering.
(CVPR), 815–823,
Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition
| URL | http://dx.doi.org/10.1109/CVPR.2015.7298682. |     |     |     |     |     |     |     |     |
| --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ShippmannJS,AshRA,BattistaM,CarrL,EydeLD,HeskethB,KehoeJ,PearlmanK,PrienEP,Sanchez
JI (2000) The practice of competency modeling. Personnel Psychology 53(3):703–740, URL http:
//dx.doi.org/10.1111/j.1744-6570.2000.tb00220.x.
Spearman C (1904) The proof and measurement of association between two things.
The American Journal
| of Psychology |     | 15(1):72–101, |     | URL | http://dx.doi.org/10.2307/1412159. |     |     |     |     |
| ------------- | --- | ------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- |

| Du et al.: | ExploringaNewCompetencyModelingProcesswithLargeLanguageModels |     |     |     |     |
| ---------- | ------------------------------------------------------------- | --- | --- | --- | --- |
21
Preprint
Stevens GW (2013) A critical review of the science and practice of competency modeling. Human Resource
Development Review 12(1):86–107, URL http://dx.doi.org/10.1177/1534484312456690.
Wei J, Tay Y, Bommasani R, Raffel C, Zoph B, Borgeaud S, Yogatama D, Bosma M, Zhou D, Metzler
D, et al. (2022) Emergent abilities of large language models. arXiv preprint arXiv:2206.07682 URL
https://arxiv.org/abs/2206.07682.
Yang A, Yang B, Zhang B, Hui B, Zheng B, Yu B, Li C, Liu D, Huang F, Wei H, et al. (2024) Qwen2.5
| technical | report. |       |                           | URL | https://arxiv.org/abs/2412.15115. |
| --------- | ------- | ----- | ------------------------- | --- | --------------------------------- |
|           |         | arXiv | preprint arXiv:2412.15115 |     |                                   |
Zhang T, Ladhak F, Durmus E, Liang P, McKeown K, Hashimoto TB (2024) Benchmarking large language
models for news summarization. Transactions of the Association for Computational Linguistics 12:39–
| 57, | URL http://dx.doi.org/10.1162/tacl_a_00586. |     |     |     |     |
| --- | ------------------------------------------- | --- | --- | --- | --- |
ZhaoWX,ZhouK,LiJ,TangT,WangX,HouY,MinY,ZhangB,ZhangJ,DongZ,etal.(2023)Asurveyof
| large    | language | models.    |                |                  | URL https://arxiv.org/abs/2303.18223. |
| -------- | -------- | ---------- | -------------- | ---------------- | ------------------------------------- |
|          |          |            | arXiv preprint | arXiv:2303.18223 |                                       |
| Appendix | A:       | Competency | Library        |                  |                                       |
In this appendix, we provide a brief description of the competency items from the Lominger and Korn Ferry
| libraries          | that are | referenced     | in Table 2     | and Table 4. |     |
| ------------------ | -------- | -------------- | -------------- | ------------ | --- |
| A.1. 67            | Longmier | Competencies   |                |              |     |
| • B: Making        |          | Complex        | Decisions      |              |     |
| 51:                | Problem  | Solving        |                |              |     |
| • C: Creating      |          | the New        | and Different  |              |     |
| • D: Keeping       |          | on Point       |                |              |     |
| • F: Getting       |          | Work Done      | Through Others |              |     |
| • I: Making        | Tough    | People         | Calls          |              |     |
| 25:                | Hiring   | and Staffing   |                |              |     |
| • L: Communicating |          |                | Effectively    |              |     |
| 67:                | Written  | Communications |                |              |     |
| • M:               | Managing | Up             |                |              |     |
| • N: Relating      |          | Skills         |                |              |     |
3: Approachability
| • P: Managing  |             | Diverse   | Relationships |     |     |
| -------------- | ----------- | --------- | ------------- | --- | --- |
| 15:            | Customer    | Focus     |               |     |     |
| 21:            | Managing    | Diversity |               |     |     |
| 23:            | Fairness    | to Direct | Reports       |     |     |
| • Q: Inspiring |             | Others    |               |     |     |
| 37:            | Negotiating |           |               |     |     |
| 60:            | Building    | Effective | Teams         |     |     |
| • R: Acting    | With        | Honor     | and Character |     |     |

Du et al.: ExploringaNewCompetencyModelingProcesswithLargeLanguageModels
22
Preprint
29: Integrity and Trust
• S: Being Open and Receptive
26: Humor
33: Listening
41: Patience
44: Personal Disclosure
• T: Demonstrating Personal Flexibility
A.2. Kon Ferry Library
• 2: Customer Focus
• 13: Directs Work
• 19: Manages Conflicts
• 20: Interpersonal Savvy
• 21: Builds Networks
• 22: Attracts Top Talent
• 23: Develops Talent
• 24: Values Differences
• 26: Communicates Effectively
• 29: Persuades
