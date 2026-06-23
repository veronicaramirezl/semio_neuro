import streamlit as st
import os

# Configuración de página estricta
st.set_page_config(page_title="Repaso de Semiología GRUNECO", page_icon="🧠", layout="centered")

# --- SECCIÓN DE INTRODUCCIÓN Y BIENVENIDA ---
# Mostrar logo si el archivo existe en la ruta especificada
logo_path = "/workspaces/semio_neuro/GRUNECO_CPT_T.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=250)

st.title("👋 Bienvenido a la página de repaso de semiología GRUNECO")
st.write(
    "Este es un espacio interactivo diseñado para que puedan autoevaluarse en los componentes clave "
    "del examen neurológico. Sigan la rúbrica oficial paso a paso para medir su desempeño técnico."
)
st.markdown(
    "Para más información, ver proyectos o conocer más del grupo, visiten nuestro sitio web oficial: "
    "[gruneco.com.co](https://gruneco.com.co)"
)
st.markdown("---")
st.markdown("### 📝 Autoevaluación del Examen Neurológico")
st.write("Selecciona **Sí** o **No** para calificar cada uno de los ítems literales del documento madre:")

# Estructura monolítica y literal de la rúbrica
DATA_RUBRICA = {
    "PARES CRANEALES: I PAR (OLFATORIO) - INSPECCIÓN Y ESPECULOSCOPIA": {
        "max": 6,
        "items": [
            "Inspecciona visualmente ambas fosas nasales",
            "Utiliza iluminación y el espéculo nasal para ver mejor",
            "Observa el dorso de la nariz para identificar desviaciones aparentes del tabique",
            "Determina el tamaño y forma de los cartílagos laterales, así como la posición y tamaño de las narinas",
            "Buscar la presencia de equimosis, hematomas, edema o excoriaciones",
            "Observar el tamaño de los cornetes inferiores, la presencia de secreciones y el estado del meato inferior (verificando si tiene salida de secreción)"
        ]
    },
    "PARES CRANEALES: I PAR (OLFATORIO) - EVALUACIÓN OLFATIVA": {
        "max": 7,
        "items": [
            "Solicita al paciente cerrar ambos ojos",
            "Pide al paciente tapar una fosa nasal",
            "Utiliza sustancias no irritantes: café, vainilla, canela y jabón neutro",
            "No utiliza alcohol o amoníaco (estimulan V par)",
            "Pregunta al paciente en cada fosa nasal si percibe el olor o es capaz de reconocerlo",
            "Evalúa ambas fosas nasales",
            "Intercambia el orden de los olores para evitar un patrón reconocible por el paciente"
        ]
    },
    "PARES CRANEALES: II PAR (ÓPTICO) - AGUDEZA VISUAL": {
        "max": 7,
        "items": [
            "Evalua primero este elemento antes que los otros aspectos",
            "Inicia la evaluación evaluando ambos ojos",
            "Posteriormente evalua cada uno de los ojos por separado",
            "Da la instrucción de forma adecuada al paciente y señalando las letras adecuadamente",
            "Cambia de línea a la siguiente si el paciente identifica todas o a la anterior si el paciente no identifica",
            "Utiliza la carta de snellen para visión lejana",
            "Utiliza la carta de rosenbaum para visión cercana"
        ]
    },
    "PARES CRANEALES: II PAR (ÓPTICO) - CAMPIMETRÍA (POR CONFRONTACIÓN)": {
        "max": 5,
        "items": [
            "Utiliza un elemento adecuado (Idealmente alfiler rojo de 5mm)",
            "Se para a la distancia adecuada (entre 50 y 70 cm)",
            "Evalua cada ojo de forma diferencial",
            "Evalúa todos los cuadrantes (laterales y mediales)",
            "Evalua la atención visual (doble estimulación simultánea)"
        ]
    },
    "PARES CRANEALES: II PAR (ÓPTICO) - FONDO DE OJO (FUNDOSCOPIA)": {
        "max": 4,
        "items": [
            "Maneja adecuadamente el oftalmoscopio (Realiza el ajuste de la corrección de agudeza visual y conoce el uso de cada uno de los tipos de luz)",
            "Se posiciona adecuadamente frente al paciente evaluando cada ojo con su similar (OD/OD-OI/OI)",
            "Logra identificar las estructuras del fondo de ojo, la papila (bordes, excavación, color), relación copa/disco, vasos (cruces AV), retina, hemorragias/exudados)",
            "Evalua cada ojo de forma diferencial"
        ]
    },
    "PARES CRANEALES: II PAR (ÓPTICO) - VISIÓN DE LOS COLORES": {
        "max": 5,
        "items": [
            "Posiciona adecuadamente las láminas del test de Ishihara a 75 cm del paciente",
            "Valora cada uno de los ojos de forma diferencial (Empezando por el ojo enfermo)",
            "Presenta las imágenes 1-2-6-10-14-18 en un ojo",
            "Presenta las imágenes 1-3-7-11-15-19 en el otro ojo",
            "Presenta todos los tipos de estímulos en cada uno de los ojos"
        ]
    },
    "PARES CRANEALES: II PAR (ÓPTICO) / III PAR - REFLEJO FOTOMOTOR": {
        "max": 7,
        "items": [
            "Utiliza un instrumento adecuado (linterna de luz dirigida o oftalmoscopio)",
            "Se posiciona adecuadamente frente al paciente",
            "Estimula cada ojo por separado y evalúa la respuesta del ojo estimulado (directo)",
            "Cubre adecuadamente el espacio nasal con la mano",
            "Describe adecuadamente el tamaño basal en milímetros, la simetría y la forma de la pupila",
            "Cubre cada uno de los ojos para ver los cambios en la contracción",
            "Describe los cambios en la pupila en situación de penumbra y luz"
        ]
    },
    "PARES CRANEALES: III, IV Y VI PAR - MOVIMIENTOS OCULARES": {
        "max": 10,
        "items": [
            "Inspecciona el rostro para identificar alteraciones (ptosis palpebral, alineación ocular primaria)",
            "Se posiciona adecuadamente frente al paciente",
            "Realiza cover-uncover test",
            "Evalua la presencia o ausencia de nistagmo (si es evocado o no)",
            "Da la instrucción de forma adecuada al paciente",
            "El desplazamiento del indicador es adecuado (Se desplaza en forma de H o en forma de asterísco)",
            "Evalua ambos ojos al mismo tiempo (movimientos conjugados)",
            "Evalua todos los movimientos en cada uno de los ojos (Sup - Inf - Lat - Med - Obl Sup - Obl Inf - Conj)",
            "Describe adecuadamente los músculos y nervios implicados en cada uno de los diferentes movimientos",
            "Evalua la acomodación / convergencia"
        ]
    },
    "PARES CRANEALES: V PAR (TRIGÉMINO) - COMPONENTE SENSITIVO": {
        "max": 12,
        "items": [
            "Evalua adecuadamente el reflejo corneal (toca cornea lateral con algodon fino, NO toca conjuntiva, observa parpadeo bilateral)",
            "Describe adecuadamente las ramas implicadas en el reflejo (Aferente V1, eferente VII)",
            "Evalua tacto superficial (roce) en rama v1 (oftálmica)",
            "Evalua tacto superficial (roce) en rama v2 (maxilar)",
            "Evalua tacto superficial (roce) en rama v3 (mandibular)",
            "Evalua sensibilidad de forma bilateral (Tacto superficial)",
            "Pregunta por identificación y localización (Tacto superficial)",
            "Evalua dolor (chuzón) en rama v1 (oftálmica)",
            "Evalua dolor (chuzón) en rama v2 (maxilar)",
            "Evalua dolor (chuzón) en rama v3 (mandibular)",
            "Evalua sensibilidad de forma bilateral (Dolor)",
            "Pregunta por identificación y localización (Dolor)"
        ]
    },
    "PARES CRANEALES: V PAR (TRIGÉMINO) - COMPONENTE MOTOR": {
        "max": 4,
        "items": [
            "Evalua el trofismo de músculos temporales y pterigoideos",
            "Evalua el trofismo de músculos maseteros",
            "Evalua la fuerza de músculos maseteros (evalúa la contracción con la mordida y la apertura contra resistencia)",
            "Evalúa el reflejo maseterino"
        ]
    },
    "PARES CRANEALES: VII PAR (FACIAL) - MÍMICA FACIAL Y GUSTO": {
        "max": 11,
        "items": [
            "Evalúa la simetría facial (Hace especial énfasis en surco nasogeniano)",
            "Pide al paciente que arrugue la frente (Imita el gesto si el paciente no entiende la instrucción)",
            "Pide al paciente frunza el ceño (Imita el gesto si el paciente no entiende la instrucción)",
            "Pide al paciente que cierre los párpados (Evalúa el lagoftalmos)",
            "Evalua fuerza de cierre de párpados",
            "Pide al paciente que arrugue la nariz (Imita el gesto si el paciente no entiende la instrucción)",
            "Pide al paciente que haga una risa grande (Imita el gesto si el paciente no entiende la instrucción)",
            "Pide al paciente que infle los cachetes (Imita el gesto si el paciente no entiende la instrucción)",
            "Evalua la fuerza al inflar los cachetes",
            "Pide al paciente que sople o tire un beso (Imita el gesto si el paciente no entiende la instrucción)",
            "Evalúa el gusto con solución azucarada (En los 2/3 anteriores de la lengua)"
        ]
    },
    "PARES CRANEALES: VIII PAR (AUDITIVO) - EVALUACIÓN DE LA AUDICIÓN": {
        "max": 4,
        "items": [
            "Se posiciona adecuadamente con las manos en ambos lados de los oídos del paciente",
            "Evalua el chasquido (roce de los dedos) en cada oído por separado",
            "Evalua el chasquido (roce de los dedos) en ambos oídos al tiempo",
            "Evalua primero este elemento antes que los otros aspectos"
        ]
    },
    "PARES CRANEALES: VIII PAR (AUDITIVO) - ESPECULOSCOPIA DE OÍDO (OTOSCOPIA)": {
        "max": 5,
        "items": [
            "Manipula adecuadamente el otoscopio",
            "Realiza adecuadamente la maniobra de tracción del pabellon auricular",
            "Inspecciona adecuadamente la trayectoria del conducto auditivo externo (Identifica signos de inflamación, cerumen, infección o secreciones)",
            "Evalúa la membrana timpánica (Integridad, bordes, color gris perla, movilidad, abombamiento y su transparencia)",
            "Identifica los puntos de referencia anatómicos (umbo u ombligo del tímpano, la apófisis larga del martillo y el cono luminoso)"
        ]
    },
    "PARES CRANEALES: VIII PAR (AUDITIVO) - PRUEBA DE WEBER": {
        "max": 4,
        "items": [
            "Manipula adecuadamente el diapasón",
            "Ubica adecuadamente el diapasón sobre la cabeza del paciente",
            "Hace vibrar / sonar adecuadamente el diapasón",
            "Pregunta al paciente por lateralización del sonido"
        ]
    },
    "PARES CRANEALES: VIII PAR (AUDITIVO) - PRUEBA DE RINNE": {
        "max": 5,
        "items": [
            "Manipula adecuadamente el diapasón (Rinne)",
            "Ubica adecuadamente el diapasón sobre la apófisis mastoide",
            "Da la instrucción adecuada al paciente",
            "Al cesar el sonido (indica el paciente) pone el diapasón en la parte externa del pabellón auricular",
            "Evalua Rinne de forma bilateral"
        ]
    },
    "PARES CRANEALES: IX PAR (GLOSOFARÍNGEO) Y X PAR (VAGO)": {
        "max": 7,
        "items": [
            "Solicita al paciente que tosa",
            "Evalúa la fonación del paciente (tres tristes tigres o treinta y tres) Describe si es disartria espástica, atáxica o flácida, presencia de voz bitonal, disfonía",
            "Evalúa la posición de la úvula",
            "Evalúa alteraciones en el paladar (Evalua elevación del paladar pidiendole que diga 'Aaaa')",
            "Evalúa el reflejo nauseoso (cuando se sospecha alteración)",
            "Evalua la deglución del paciente (solicitar que trague)",
            "Evalúa el gusto (1/3 posterior)"
        ]
    },
    "PARES CRANEALES: XI PAR (ESPINAL ACCESORIO)": {
        "max": 3,
        "items": [
            "Evalua la flexión del cuello y extensión de la cabeza de cada lado (se puede agregar rotación)",
            "Evalua la elevación y descenso de los hombros",
            "Evalua inicialmente de forma libre y posteriormente poniendo resistencia"
        ]
    },
    "PARES CRANEALES: XII PAR (HIPOGLOSO)": {
        "max": 4,
        "items": [
            "Utiliza iluminación para observar la lengua",
            "Evalúa el trofismo de la lengua (reporta si identifica la presencia de fasciculaciones o desviaciones)",
            "Evalúa los movimientos de la lengua de forma libre inicialmente",
            "Pone resistencia para evaluar la fuerza de los movimientos (Utiliza bajalenguas o fuerza contra la mejilla)"
        ]
    },
    "SENSIBILIDAD SUPERFICIAL - TACTO FINO EXTREMIDAD SUPERIOR": {
        "max": 6,
        "items": [
            "Evalúa Hombro, cara posterior del brazo y parte superior del tórax - Supraclavicular - C4 (Tacto fino)",
            "Evalúa Región lateral del hombro y cara externa (superior) del brazo - Deltoides C5 (Tacto fino)",
            "Evalúa Lado lateral (radial) del antebrazo, dedo pulgar e índice - C6 (Tacto fino)",
            "Evalúa Dedo medio - C7 (Tacto fino)",
            "Evalúa Lado medial (cubital) del antebrazo, dedo anular y meñique - C8 (Tacto fino)",
            "Evalúa Región medial y superior del antebrazo (cara interna/axila) - T1 (Tacto fino)"
        ]
    },
    "SENSIBILIDAD SUPERFICIAL - OBSERVACIONES DE TÉCNICA EXTREMIDAD SUPERIOR": {
        "max": 6,
        "items": [
            "Se asegura que el paciente esté alerta (Extremidad superior)",
            "Solicita al paciente que cierre y mantenga los ojos cerrados (Extremidad superior)",
            "Valida para cada segmento que el paciente refiera si sintió o no la estimulación (Extremidad superior)",
            "Pregunta al paciente por el tipo de estímulo que recibió (Extremidad superior)",
            "Solicita al paciente que describa o señale el lugar en el que sintió la estimulación (Pregunta por la lateralidad - Extremidad superior)",
            "Evalúa la simetría entre ambas extremidades en el mismo segmento (Extremidad superior)"
        ]
    },
    "SENSIBILIDAD SUPERFICIAL - DOLOR EXTREMIDAD SUPERIOR": {
        "max": 7,
        "items": [
            "Evalúa Hombro, cara posterior del brazo y parte superior del tórax - Supraclavicular - C4 (Dolor)",
            "Evalúa Región lateral del hombro y cara externa (superior) del brazo - Deltoides C5 (Dolor)",
            "Evalúa Lado lateral (radial) del antebrazo, dedo pulgar e índice - C6 (Dolor)",
            "Evalúa Dedo medio - C7 (Dolor)",
            "Evalúa Lado medial (cubital) del antebrazo, dedo anular y meñique - C8 (Dolor)",
            "Evalúa Región medial y superior del antebrazo (cara interna/axila) - T1 (Dolor)",
            "Presiona levemente el objeto punzante sobre la piel"
        ]
    },
    "SENSIBILIDAD SUPERFICIAL - DISCRIMINACIÓN TÉRMICA EXTREMIDAD SUPERIOR": {
        "max": 7,
        "items": [
            "Evalúa Hombro, cara posterior del brazo y parte superior del tórax - Supraclavicular - C4 (Temperatura)",
            "Evalúa Región lateral del hombro y cara externa (superior) del brazo - Deltoides C5 (Temperatura)",
            "Evalúa Lado lateral (radial) del antebrazo, dedo pulgar e índice - C6 (Temperatura)",
            "Evalúa Dedo medio - C7 (Temperatura)",
            "Evalúa Lado medial (cubital) del antebrazo, dedo anular y meñique - C8 (Temperatura)",
            "Evalúa Región medial y superior del antebrazo (cara interna/axila) - T1 (Temperatura)",
            "Evalúa la discriminación térmica con dos referencias distintas (Parte goma y parte metálica del martillo)"
        ]
    },
    "SENSIBILIDAD SUPERFICIAL - TACTO FINO EXTREMIDAD INFERIOR": {
        "max": 6,
        "items": [
            "Evalúa Región de la ingle y área hipogástrica - L1 (Tacto fino)",
            "Evalúa Cara anterior y lateral del muslo - L2 (Tacto fino)",
            "Evalúa Cara anterior e inferior del muslo y región de la rodilla - L3 (Tacto fino)",
            "Evalúa Cara medial (interna) de la pierna hasta el maléolo medial - L4 (Tacto fino)",
            "Evalúa Cara lateral de la pierna y dorso del pie (especialmente el dedo gordo) - L5 (Tacto fino)",
            "Evalúa Borde lateral del pie y quinto dedo (dedo pequeño) - S1 (Tacto fino)"
        ]
    },
    "SENSIBILIDAD SUPERFICIAL - OBSERVACIONES DE TÉCNICA EXTREMIDAD INFERIOR": {
        "max": 8,
        "items": [
            "Evalúa Cara posterior del muslo y de la pierna - S2 (Tacto fino)",
            "Evalúa Región perineal y perianal (distribución 'en silla de montar') - S3 - S5",
            "Se asegura que el paciente esté alerta (Extremidad inferior)",
            "Solicita al paciente que cierre y mantenga los ojos cerrados (Extremidad inferior)",
            "Valida para cada segmento que el paciente refiera si sintió o no la estimulación (Extremidad inferior)",
            "Pregunta al paciente por el tipo de estímulo que recibió (Extremidad inferior)",
            "Solicita al paciente que describa o señale el lugar en el que sintió la estimulación (Pregunta por la lateralidad - Extremidad inferior)",
            "Evalúa la simetría entre ambas extremidades en el mismo segmento (Extremidad inferior)"
        ]
    },
    "SENSIBILIDAD SUPERFICIAL - DOLOR EXTREMIDAD INFERIOR": {
        "max": 7,
        "items": [
            "Evalúa Región de la ingle y área hipogástrica - L1 (Dolor)",
            "Evalúa Cara anterior y lateral del muslo - L2 (Dolor)",
            "Evalúa Cara anterior e inferior del muslo y región de la rodilla - L3 (Dolor)",
            "Evalúa Cara medial (interna) de la pierna hasta el maléolo medial - L4 (Dolor)",
            "Evalúa Cara lateral de la pierna y dorso del pie (especialmente el dedo gordo) - L5 (Dolor)",
            "Evalúa Borde lateral del pie y quinto dedo (dedo pequeño) - S1 (Dolor)",
            "Presiona levemente el objeto punzante sobre la piel (Miembro inferior)"
        ]
    },
    "SENSIBILIDAD SUPERFICIAL - DISCRIMINACIÓN TÉRMICA EXTREMIDAD INFERIOR": {
        "max": 7,
        "items": [
            "Evalúa Región de la ingle y área hipogástrica - L1 (Temperatura)",
            "Evalúa Cara anterior y lateral del muslo - L2 (Temperatura)",
            "Evalúa Cara anterior e inferior del muslo y región de la rodilla - L3 (Temperatura)",
            "Evalúa Cara medial (interna) de la pierna hasta el maléolo medial - L4 (Temperatura)",
            "Evalúa Cara lateral de la pierna y dorso del pie (especialmente el dedo gordo) - L5 (Temperatura)",
            "Evalúa Borde lateral del pie y quinto dedo (dedo pequeño) - S1 (Temperatura)",
            "Evalúa la discriminación térmica con dos referencias distintas (Parte goma y parte metálica del martillo - M. Inferior)"
        ]
    },
    "SENSIBILIDAD PROFUNDA - VIBRACIÓN (PALESTESIA)": {
        "max": 7,
        "items": [
            "Evalúa en el codo",
            "Evalúa en las muñecas",
            "Evalúa en la rodilla",
            "Evalúa en el tobillo",
            "Agarra el diapasón del mango (sin tocar los brazos del diapasón) y lo pone a vibrar adecuadamente",
            "Ubica adecuadamente el diapasón sobre la prominencia ósea con una leve presión",
            "Evalúa la simetría entre ambas extremidades en el mismo segmento (Palestesia)"
        ]
    },
    "SENSIBILIDAD PROFUNDA - SENTIDO DE POSICIÓN (BATIESTESIA)": {
        "max": 5,
        "items": [
            "Evalúa en el miembro superior (Dedo de la mano)",
            "Evalúa en el miembro inferior (Dedo del pie)",
            "Desplazan pasivamente los dedos o artejos del paciente",
            "Le pide al paciente que identifique la dirección del movimiento",
            "Realiza movimientos alternantes para evitar un patrón"
        ]
    },
    "SENSIBILIDAD CORTICAL - ESTEREOGNOSIA": {
        "max": 5,
        "items": [
            "Reconocimiento de objetos comunes con el tacto",
            "Se asegura que la sensibilidad primaria esté intacta (tacto, vibración) - Estereognosia",
            "Realiza la evaluación independiente de cada mano",
            "Evalúa de forma bilateral (Estereognosia)",
            "Presenta diferentes objetos para evitar que el paciente los aprenda"
        ]
    },
    "SENSIBILIDAD CORTICAL - GRAFESTESIA": {
        "max": 6,
        "items": [
            "Reconocimiento de patrones realizados en trazos sobre la piel",
            "Realiza la evaluación en diferentes segmentos (Grafestesia)",
            "Evalúa de forma bilateral (Grafestesia)",
            "Realiza trazos continuos y con figuras simples que el paciente pueda reconocer",
            "Documenta si el paciente logra sólo describir, identificar o si confunde los objetos.",
            "Da un tiempo prudente de entre 5 a 10 segundos"
        ]
    },
    "SENSIBILIDAD CORTICAL - DISCRIMINACIÓN DE DOS PUNTOS": {
        "max": 5,
        "items": [
            "Capacidad de distinguir dos estímulos cercanos",
            "Realiza la evaluación en diferentes segmentos (pulpejos, palma, antebrazos, dorso mano o espalda)",
            "Evalúa de forma bilateral (Discriminación 2 puntos)",
            "Identifica como normal la discriminación de 2 a 4 mm en pulpejos",
            "Se asegura que la sensibilidad primaria esté intacta (tacto, vibración) - Discriminación de dos puntos"
        ]
    },
    "SENSIBILIDAD CORTICAL - BAROGNOSIA": {
        "max": 5,
        "items": [
            "Capacidad de reconocer o distinguir el peso de un objeto",
            "Realiza la evaluación en diferentes segmentos (pulpejos, antebrazos y espalda) - Barognosia",
            "Evalúa de forma bilateral (Barognosia)",
            "Identifica como normal la discriminación de 2 a 4 mm en pulpejos, 2-3 cm dorso mano, 4 cm en antebrazo, 7 cm en espalda",
            "Solicita al paciente que cierre y mantenga los ojos cerrados (Barognosia)"
        ]
    },
    "SENSIBILIDAD CORTICAL - FENÓMENO DE EXTINCIÓN": {
        "max": 4,
        "items": [
            "Estimulación simultánea en puntos homólogos en ambos lados",
            "Realiza la evaluación estimulando al tiempo dos sitios homólogos en ambos",
            "Reconoce que la identificación por parte del paciente de uno de los puntos indica lesión parietal contralateral",
            "Se asegura que la sensibilidad primaria esté intacta (tacto, vibración) - Extinción"
        ]
    },
    "FUERZA SEGMENTARIA - MIEMBRO SUPERIOR": {
        "max": 9,
        "items": [
            "Evalúa Brazo - Naducción (Acercar) / Abducción (Alejar) / Rotación interna / Rotación externa",
            "Evalúa Antebrazo - Flexión / Extensión",
            "Evalúa Mano - Flexión / Extensión / Presión",
            "Evalúa Dedos - apertura / cierre",
            "Inspecciona para evaluar el trofismo y observa para identificar asimetrías en los grupos musculares",
            "Palpa la extremidad para evaluar el tono y la consistencia de los grupos musculares (M. Superior)",
            "Evalúa adecuadamente la escala de Daniels o MRC (M. Superior)",
            "Evalúa que se tenga contracción muscular y desplazamiento horizontal sin o con resistencia",
            "Hace una valoración de la fuerza proximal y distal (M. Superior)"
        ]
    },
    "FUERZA SEGMENTARIA - MIEMBRO INFERIOR": {
        "max": 9,
        "items": [
            "Evalúa Muslo - Abducción (Alejar) / Aducción (Acercar) / Flexión / Extensión",
            "Evalúa Pierna - flexión / Extensión",
            "Evalúa Pie - Flexión / Extensión / Eversión / Inversión",
            "Evalúa Dedo - Flexión / Extensión",
            "Inspecciona para evaluar el trofismo y observa para identificar asimetrías (M. Inferior)",
            "Palpa la extremidad para evaluar el tono y la consistencia (M. Inferior)",
            "Evalúa adecuadamente la escala de Daniels o MRC (M. Inferior)",
            "Ofrece diferentes niveles de resistencia al paciente / Deja espacio para el movimiento voluntario",
            "Hace una valoración de la fuerza proximal y distal (M. Inferior)"
        ]
    },
    "REFLEJOS MUSCULOTENDINOSOS (OSTEOTENDINOSOS)": {
        "max": 8,
        "items": [
            "Maseterino / Tricipital / Bicipital / Estiloradial / Rotuliano-Patelar / Aquiliano",
            "En el maseterino golpea sobre dedo índice sobre la mandíbula con la boca ligeramente abierta",
            "En el tricipital golpea en tendon del triceps, golpe encima del olécranon y colgando el brazo",
            "En el bicipital dedo del evaluador por encima del tendón",
            "En estiloradial golpe en apófisis estiloides",
            "En el rotuliano golpe en ligamento rotuliano, lo palpa y encuentra adecuadamente previamente",
            "En el Aquiliano golpea con el pie en ligera dorsiflexión",
            "Evita autosugestión del paciente y realiza el golpe o estimulación perpendicular al tendón"
        ]
    },
    "REFLEJOS PATOLÓGICOS": {
        "max": 7,
        "items": [
            "Glabelar / Succión / Palmomentoniano (Marinesco) / Hoffman (Lecho Ungueal) / Presión palmar / Reflejo cutáneo plantar (Signo de Babinsky)",
            "En glabelar golpea la glabela repetidamente y evalúa si es agotable o no",
            "En succión estimula labio superior and lo reconoce como Signos de liberación frontal",
            "En palmomentoniano Estimula la palma (puede ser con la punta del martillo)",
            "En hoffman Golpea adecuadamente la uña",
            "En presión palmar Golpea borde cubital o palmar",
            "En Babinski realiza la estimulación desde borde lateral hasta base del segundo dedo e identifica la flexión/extensión"
        ]
    },
    "COORDINACIÓN SENTADO - MANIOBRA DEDO-NARIZ": {
        "max": 9,
        "items": [
            "Maniobra dedo - nariz",
            "Se posiciona frente al paciente (Dedo-nariz)",
            "Da la instrucción de forma clara (Dedo-nariz)",
            "Inicia con el dedo del paciente en nariz",
            "Sigue con movimiento al dedo del evaluador",
            "Realiza movimientos del dedo para evaluar seguimiento",
            "Evaluar primero lento y luego rápido",
            "Evalua la maniobra con los ojos cerrados (Nariz)",
            "Evalua con ojos cerrados y abiertos (Identifica error: ataxia sensitiva vs cerebelosa) de forma bilateral"
        ]
    },
    "COORDINACIÓN SENTADO - TALÓN-RODILLA": {
        "max": 5,
        "items": [
            "Talón - Rodilla",
            "Solicita al paciente ubicar su talon en la rodilla contraria e indica que baje hasta el tobillo (Forma controlada)",
            "Le indica al paciente hacer la maniobra de forma libre",
            "Evalua con los ojos del paciente cerrados",
            "Evalua de forma bilateral (Talón-rodilla)"
        ]
    },
    "COORDINACIÓN SENTADO - PRONACIÓN-SUPINACIÓN": {
        "max": 5,
        "items": [
            "Pronación - Supinación",
            "Pide al paciente afrontar ambas palmas (una supina y la otra prono) dejando la inferior quieta",
            "Pide al paciente alternar prono supino en la mano superior",
            "Corrige e indica si se realiza mal por el paciente",
            "Evalua de forma bilateral (Prono-supino)"
        ]
    },
    "COORDINACIÓN SENTADO - AFRONTAMIENTO DE LOS DEDOS": {
        "max": 5,
        "items": [
            "Afrontamiento de los dedos",
            "Da la instrucción al paciente (Afrontamiento)",
            "Inicia con índice y pulgar",
            "Evalúa la velocidad de ejecución e intercambia entre los dedos",
            "Evalúa de forma bilateral (Afrontamiento)"
        ]
    },
    "COORDINACIÓN EN BIPEDESTACIÓN - MANIOBRA DE ROMBERG": {
        "max": 5,
        "items": [
            "Maniobra de Romberg",
            "Pide al paciente juntar los pies",
            "Evalua la fase de ojos abiertos (cerebelo)",
            "Pide al paciente cerrar los ojos y evalúa la fase (propiocepción/vestibular)",
            "Garantiza la seguridad del paciente (Romberg)"
        ]
    },
    "MARCHA - LÍNEA RECTA": {
        "max": 7,
        "items": [
            "Marcha en línea Recta",
            "Indica la línea guía al paciente",
            "Evalúa la base de sustentación, la velocidad y el ritmo de la marcha",
            "Observa el balanceo de los brazos",
            "Observa la simetría de la marcha (No lateralización)",
            "Garantiza la seguridad del paciente (Línea recta)",
            "Ejecución técnica completa de los ítems de control"
        ]
    },
    "MARCHA - TÁNDEM": {
        "max": 4,
        "items": [
            "Marcha en Tándem",
            "Da la indicación al paciente (Tándem)",
            "Evalúa la estabilidad e identifica que se utiliza para evaluar vermis cerebeloso y ataxia truncal",
            "Garantiza la seguridad del paciente (Tándem)"
        ]
    },
    "MARCHA - PUNTA DE PIE": {
        "max": 4,
        "items": [
            "Marcha en punta de pie",
            "Da la indicación al paciente (Punta de pie)",
            "Evalúa de forma bilateral e identifica que se utiliza para evaluar S1 y funcionales",
            "Garantiza la seguridad del paciente (Punta de pie)"
        ]
    },
    "MARCHA - TALÓN": {
        "max": 4,
        "items": [
            "Marcha en talón",
            "Da la indicación al paciente (Talón)",
            "Evalúa de forma bilateral e identifica que se utiliza para evaluar L4 y L5 y funcionales",
            "Garantiza la seguridad del paciente (Talón)"
        ]
    },
    "MARCHA - PATASOLA": {
        "max": 6,
        "items": [
            "Marcha en patasola",
            "Da la indicación al paciente e inicia con fase estática",
            "Evalúa desplazamiento de forma bilateral",
            "Identifica que se utiliza para evaluar equilibrio y en debilidad proximal",
            "Garantiza la seguridad del paciente (Patasola)",
            "Cumple la totalidad de las observaciones de la técnica"
        ]
    }
}

puntos_totales_maximos = sum(bloque["max"] for bloque in DATA_RUBRICA.values())
puntos_totales_logrados = 0

# Renderizar secciones con bullet points interactivos limpios
for titulo_seccion, datos in DATA_RUBRICA.items():
    with st.container():
        st.subheader(f"📋 {titulo_seccion}")
        subtotal_seccion = 0
        
        for item in datos["items"]:
            col_texto, col_opciones = st.columns([0.75, 0.25])
            with col_texto:
                # Se eliminó la etiqueta de texto fija, mostrando el ítem directamente como viñeta limpia
                st.markdown(f"• {item}")
            with col_opciones:
                opcion = st.radio(
                    label=item,
                    options=["No", "Sí"],
                    index=0,
                    horizontal=True,
                    label_visibility="collapsed",
                    key=f"radio_{titulo_seccion}_{item}"
                )
                if opcion == "Sí":
                    subtotal_seccion += 1
                    
        # Control estricto de subtotales
        puntos_finales_seccion = min(subtotal_seccion, datos["max"])
        puntos_totales_logrados += puntos_finales_seccion
        
        st.markdown(f"**Ejecución técnica - Total realizados:** `{puntos_finales_seccion} / {datos['max']}`")
        st.markdown("---")

# --- SECCIÓN DE RESULTADOS COMPUESTOS ---
st.subheader("📊 Calificación Final Compuesta")

nota_global = (puntos_totales_logrados / puntos_totales_maximos) * 5.0

col_puntos, col_nota = st.columns(2)
with col_puntos:
    st.metric(label="Puntos Acumulados", value=f"{puntos_totales_logrados} / {puntos_totales_maximos}")
with col_nota:
    if nota_global >= 3.5:
        st.success(f"### Nota Global: **{nota_global:.2f} / 5.0**")
    else:
        st.error(f"### Nota Global: **{nota_global:.2f} / 5.0**")

st.progress(puntos_totales_logrados / puntos_totales_maximos)
