## Project Context
__Problem Statement:__<br>
Eres un data analyst que se acaba de unir a Fit.ly Tech, una app de fitness con subscripción y recibiste un mail de tu manager con un nuevo task.
<br>

__Contexto sobre el problema:__ <br>
- En los últimos 2 trimestres han notado churn creciendo en su base de clientes.
- Es critico retener clientes porque su costo de adquisición de clientes está creciendo y cada empleado que nos deja pone más presión en marketing y producto
- __Necesitamos una foto clara de que está provocando el churn y algunas acciones practicas que podemos realizar de cara al siguiente trimestre__
- Traemos un dataset de diferentes fuentes (actividad de usuarios, soporte al cliente e información de cuentas).La data está desordenada, pues viene de diferentes equipos que usan diferentes convenciones.
- Usa esta data como punto de partida para un análisis de churn, __asegurate de incluir engagement, support activity y plan type__, pues son cosas de las que el negocio se preocupa. Enfócate en identificar patrones y potenciales drivers del churn y algunos otros KPIs que creas que nuestros lideres le prestaran atención.
- __Haz el análisis y escribe un reporte corto para el manager.__ El no necesita ver el código, pero quiere ver el pensamiento, como manejaste la limpieza de datos y la interpretación y como llegaste a tus conclusiones
- Prepara y entrega la presentación a senior leadership. Recuerda que ellos no son data specialists y se van a enfocar en que pueden hacer ellos para identificar/atacar el problema del churn.
- El jefe está de vacaciones, si necesitas tomar decisiones, incluyelas en el trabajo y los revisará cuando esté de regreso.

__Contexto sobre la data:__ <br>
Lo que dijo el Lead Engineer: <br>
- Cada dataset viene de una fuente diferente. historicamente estos fueron construidos independientemente por cada equipo, entonces el lead engineer no sabe si tienen prácticas de estandarización o validación, __no estaría sorprendido de escuchar información sobre data faltante o no estandarizada, pues los sistemas se caen de vez en cuando.__
- Ellos no hacen limpieza,trasformación ni anonimización como parte de los pipelines. Lo único que hacen es calcular el tiempo de resolución de los tickets en ETL.
- Cada dataset se actualiza diario
- Data faltante o irregular puede ocurrir si algun sistema de carga de datos experimenta downtime. Ellos automáticamente no rellenan los gaps al menos que haya un incidente mayor
- La ubicación de todos los campos está basada en información de billing del usuario.
Guide to Analysis Projects
1. I would like you to create a written report to summarize the analysis you have
performed and your findings. The report will be read by me (Head of Analysis). The list
below describes what I expect to see in your written report.
2. You will need to use a DataLab workbook to write up your findings and share
visualizations.
3. You must use the data provided for the analysis.
4. You will also need to prepare and deliver a presentation. You should prepare around
8-10 slides to present to senior leadership. The list below describes what they expect to
see in your presentation.
5. Your presentation should be no longer than 10 minutes.

Written Report
Your written report should include written text summaries and graphics of the following:
2
- Data validation:
    - Describe validation and cleaning steps for every column in the data
- Exploratory Analysis to answer the customer questions ensuring you include:
   - Two different types of graphic showing single variables only
   - At least one graphic showing two or more variables
   - Description of your findings
- Definition of a metric for the business to monitor
    - How should the business monitor what they want to achieve?
    - Estimate the initial value(s) for the metric based on the current data?
    - Final summary including recommendations that the business should undertake

Presentation <br>
You will give an overview presentation to senior leadership. The presentation should include:
- An overview of the project and business goals
- A summary of the work you undertook and how this addresses the problem
- Your key findings including the metric to monitor and current estimation
- Your recommendations to the business
