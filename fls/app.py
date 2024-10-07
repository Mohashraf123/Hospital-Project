from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/dna.html')
def index():
   return render_template('/dna.html')

@app.route('/dna',methods=['post'])

def getvalue():
  
   seq=request.form['seq']

   def countingnuc(seq):
    ns={'A':0,'C':0,'G':0,'T':0}
    for n in seq:
        ns[n]=ns[n]+1
    return ns ,sum(ns.values())
   R=countingnuc(seq)
   
   def dnatorna(seq):
    return seq.replace('T','U')
   rna=dnatorna(seq)     
   
   def complement(dnaseq):
    comp=''
    for n in dnaseq:
        if n=='A':
          comp=comp+'T'
        if n=='T':
          comp=comp+'A'
        if n=='G':
          comp=comp+'C'
        if n=='C':
          comp=comp+'G'
    return comp
   comp=complement(seq)
   
   codons={
    "GCU":"A",
    "GCC":"A",
    "GCA":"A",
    "GCG":"A",
    "UGU":"C",
    "UGC":"C",
    "GAU":"D", 
    "GAC":"D",
    "GAA":"E", 
    "GAG":"E",
    "UUU":"F", 
    "UUC":"F",
    "GGU":"G", 
    "GGC":"G", 
    "GGA":"G", 
    "GGG":"G",
    "CAU":"H", 
    "CAC":"H",
    "AUA":"I", 
    "AUU":"I", 
    "AUC":"I",
    "AAA":"K", 
    "AAG":"K",
    "UUA":"L", 
    "UUG":"L", 
    "CUU":"L", 
    "CUC":"L", 
    "CUA":"L", 
    "CUG":"L",
    "AUG":"M",
    "AAU":"N", 
    "AAC":"N",
    "CCU":"P", 
    "CCC":"P", 
    "CCA":"P", 
    "CCG":"P",
    "CAA":"Q", 
    "CAG":"Q",
    "CGU":"R", 
    "CGC":"R", 
    "CGA":"R", 
    "CGG":"R", 
    "AGA":"R",
    "AGG":"R",
    "UCU":"S", 
    "UCC":"S", 
    "UCA":"S", 
    "UCG":"S", 
    "AGU":"S", 
    "AGC":"S",
    "ACU":"T", 
    "ACC":"T", 
    "ACA":"T", 
    "ACG":"T",
    "GUU":"V", 
    "GUC":"V", 
    "GUA":"V", 
    "GUG":"V",
    "UGG":"W",
    "UAU":"Y",
    "UAC":"Y",
    "UAA":"Stop",
    "UAG":"Stop",
    "UGA":"Stop",
    "A":"Stop",
    "U":"Stop",
    "G":"Stop",
    "C":"Stop",
    "AA":"Stop",
    "UU":"Stop",
    "GG":"Stop",
    "CC":"Stop",  
}

   def translating(seq):
    amino=''
    for i in range(0,len(seq),3):
        if codons[seq[i:i+3]]!="Stop":
         amino= amino +codons[seq[i:i+3]]
         if codons[seq[i:i+3]]=="stop":
           break
    return amino    
   prot=translating(rna)  
   return render_template('/pass.html',seq=seq,num=R,RNA=rna,COMP=comp,protien=prot)
 
@app.route('/disease.html')
def disease():
   return render_template('/disease.html')

@app.route('/dise',methods=['post'])
def get():
  
  text =request.form['paseq']
  pattern = request.form['disseq']
  def search(text,pattern):
    if pattern in text:
      p=("the result is positive you must come to hospital to perform the necessary analyzes to follow up on any symptoms of the disease, in order to be treated as its inception ,and treatment process is completed faster")
      return True,p
    elif pattern not in text:
      p=("the result is negative")
      return False,p
    if text=="":
      return None
  f=search(text,pattern)  
  
  return render_template('/result.html',Re=f)  


@app.route('/revers.html')
def revers():
   return render_template('/revers.html') 
 
@app.route('/reve',methods=['post']) 
def re():
     data = request.form['file']
     dta=open(data,"r")
     sequn=dta.readline()
        
     def complement(dnaseq):
       comp=''
       for n in dnaseq:
        if n=='A':
          comp=comp+'T'
        if n=='T':
          comp=comp+'A'
        if n=='G':
          comp=comp+'C'
        if n=='C':
          comp=comp+'G'
       return comp
     comp=complement(sequn)
     return render_template('/rev.html',R=sequn,C=comp)

if __name__=='__main__':
    app.run(debug=True)