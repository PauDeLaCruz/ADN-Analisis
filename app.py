from flask import Flask, render_template, request

from bio_seq import bio_seq

app = Flask(__name__)

#INICIO
@app.route("/")
def index():
    return render_template('index.html')

#CONVERSION NCBI A FORMATO ADECUADO
@app.route("/conversion/", methods=['POST','GET'])
def conversion():
    return render_template('conversion.html')

#CONVERSION NCBI A FORMATO ADECUADO - RESULTADOS
@app.route("/conversionexitosa/", methods=['POST','GET'])
def conversionexitosa():
    if request.method == 'POST':
        secuenciancbi = request.form['secuenciancbi']
        for i in " \n0123456789":
            secuenciancbi = secuenciancbi.replace(i, "")
        return render_template('conversionexitosa.html',secuenciancbi=secuenciancbi)

#GENERAR SECUENCIA ALEATORIA
@app.route("/generar/", methods=['POST','GET'])
def generar():
    return render_template('generar.html')

#GENERAR SECUENCIA ALEATORIA - RESULTADO
@app.route("/secuenciagenerada/", methods=['POST','GET'])
def secuenciagenerada():
    valorusuario = int(request.form['valorusuario'])
    test_dna = bio_seq()
    test_dna.generate_rnd_seq(valorusuario, "DNA")
    info = test_dna.get_seq_info_array()
    return render_template('secuenciagenerada.html', info=info)

#ANALISIS DE SECUENCIAS
@app.route("/analizar/", methods=['GET','POST'])
def analizar():
    return render_template('analizar.html')
        
#ANALISIS DE SECUENCIAS - RESULTADO
@app.route("/resultados/", methods=['POST','GET'])
def resultados():
    if request.method == 'POST':
        secuenciausuario = request.form['secuenciausuario']
        secuenciausuariostrip = secuenciausuario.strip()
        secuenciadefinitiva = secuenciausuariostrip.replace(" ", "")
        test_dna = bio_seq(secuenciadefinitiva)
        info = test_dna.get_seq_info_array()
        nucleotidefrequency = test_dna.nucleotide_frequency()
        transcription = test_dna.transcription()
        reversecomplement = test_dna.reverse_complement()
        gccontent = test_dna.gc_content()
        translateseq = test_dna.translate_seq()
        codonusage= test_dna.codon_usage('L')
        return render_template('datossecuencia.html', info=info, nucleotidefrequency=nucleotidefrequency, transcription=transcription, reversecomplement=reversecomplement,gccontent=gccontent,translateseq=translateseq,codonusage=codonusage)

#ANALISIS DE SECUENCIAS - TEXTO
@app.route("/descarga", methods=['POST','GET'])
def descarga():
    if request.method == 'POST':
        secuenciausuario = request.form['secusuario']
        secuenciausuario = secuenciausuario.strip()
        test_dna = bio_seq(secuenciausuario)
        info = test_dna.get_seq_info_array()
        nucleotidefrequency = test_dna.nucleotide_frequency()
        transcription = test_dna.transcription()
        reversecomplement = test_dna.reverse_complement()
        gccontent = test_dna.gc_content()
        translateseq = test_dna.translate_seq()
        codonusage= test_dna.codon_usage('L')
        return render_template('resultadostxt.html', info=info, nucleotidefrequency=nucleotidefrequency, transcription=transcription, reversecomplement=reversecomplement,gccontent=gccontent,translateseq=translateseq,codonusage=codonusage)

#GITHUB CODIGO
@app.route("/github", methods=['POST','GET'])
def github():
    return render_template("github.html")

@app.errorhandler(500)
def internal_sever_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run()
    