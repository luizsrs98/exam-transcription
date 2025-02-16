import re

def formatar_exames(texto):
    abreviacoes = {
        "ALBUMINA": "ALB",
        "CREATININA": "CRE",
        "UREIA": "URE",
        "CÁLCIO": "CAL",
        "POTÁSSIO": "POT",
        "MAGNÉSIO": "MAG",
        "Hemácias": "HEM",
        "Hemoglobina": "HGB",
        "Hematócrito": "HTO",
        "VCM": "VCM",
        "HCM": "HCM",
        "CHCM": "CHCM",
        "RDW-CV": "RDW",
        "Leucócitos": "LEU",
        "Neutrófilos": "NEU",
        "Eosinófilos": "EOS",
        "Basófilos": "BAS",
        "Monócitos": "MON",
        "Linfócitos": "LIN",
        "Exame qualitativo de urina": "EQU",
        "Proteínas": "PROT",
        "Glicose": "GLI",
        "Acetona": "ACE",
        "Hemoglobina": "HB",
        "Billirubina": "BIL",
        "Esterase leucocitária": "EST",
        "Nitrito": "NIT"
    }
    
    exames = re.findall(r"([A-ZÇÁÉÍÓÚÃÕÊÂÔ]+(?: [A-ZÇÁÉÍÓÚÃÕÊÂÔ]+)*)[^
]*?([\d,\.]+)", texto)
    
    resultado_formatado = " // ".join([f"{abreviacoes.get(exame, exame)} {valor}" for exame, valor in exames])
    
    return resultado_formatado

# Exemplo de uso
texto_exames = """
ALBUMINA Valor de Referê // 3,4 g/dL //
CREATININA Valor de Referê // 1,19 mg/dL //
UREIA Valor de Referê // 28 mg/dL //
CÁLCIO Valor de Referê // 8,4 mg/dL //
POTÁSSIO Valor de Referê // 2,3 mmol/L //
MAGNÉSIO Valor de Referê // 1,3 mg/dL //
Hemácias 2,8 milhões/mm³ //
Hemoglobina 8,6 g/dL //
Hematócrito 24,8 % //
VCM 89 fL //
HCM 30,8 pg //
CHCM 34,7 g/dL //
RDW-CV 13,4 % //
Leucócitos 8370 /mm³ //
Neutrófilos 65 5440 //
Eosinófilos 2 167 //
Basófilos 0 0 //
Monócitos 8 669 //
Linfócitos 25 2092 //
Exame qualitativo de urina // Proteínas Traços // Glicose Não reagente // Acetona Não reagente // Hemoglobina Não reagente // Billirubina Não reagente // Esterase leucocitária Não reagente // Nitrito Não reagente //
"""

print(formatar_exames(texto_exames))
