from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path
import urllib.request,re,json
root=Path(__file__).resolve().parent.parent/'dist'
assets=root/'assets'; fonts=assets/'fonts'; fonts.mkdir(exist_ok=True)
css=urllib.request.urlopen('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900').read().decode()
for weight,url in re.findall(r'font-weight: (\d+);\s*src: url\(([^)]+)',css):
 p=fonts/f'montserrat-{weight}.ttf'
 if not p.exists(): urllib.request.urlretrieve(url,p)
W,H=900,1273
C={'paper':'#fff9f5','plum':'#301c2b','rose':'#ad6683','light':'#eed7df','ink':'#392333','muted':'#715363'}
def font(size,bold=600):return ImageFont.truetype(str(fonts/f'montserrat-{bold}.ttf'),size)
def text(d,xy,t,size=25,color='ink',bold=600,spacing=9):
 d.multiline_text(xy,t,font=font(size,bold),fill=C.get(color,color),spacing=spacing)
def line(d,y):d.line((65,y,835,y),fill='#d8bac9',width=2)
def base(n,subtitle,dark=False):
 im=Image.new('RGB',(W,H),C['plum' if dark else 'paper']);d=ImageDraw.Draw(im)
 text(d,(65,48),'SEU SALÃO  /  HAIR STUDIO',17,'light' if dark else 'rose',700)
 d.line((65,88,835,88),fill=C['rose'],width=2)
 text(d,(65,1200),subtitle.upper(),14,'light' if dark else 'muted',700)
 text(d,(785,1196),f'{n:02}',23,'light' if dark else 'rose',800)
 return im,d
photo=Image.open(assets/'hair.webp').convert('RGB')
def photo_at(im,box):
 x,y,w,h=box;im.paste(ImageOps.fit(photo,(w,h),centering=(.5,.42)),(x,y))
def label(d,y,number,title,body):
 text(d,(65,y),number,26,'rose',800);text(d,(125,y),title,28,'ink',800)
 text(d,(125,y+49),body,21,'muted',500,spacing=10)

im,d=base(1,'Seu talento. Sua marca. Sua apresentação.',True)
text(d,(65,140),'CATÁLOGO',62,'light',900);text(d,(65,212),'DE SERVIÇOS',62,'paper',900)
text(d,(65,315),'Seu cabelo,\nsua melhor versão.',37,'light',700,spacing=7)
photo_at(im,(65,450,770,640))
d=ImageDraw.Draw(im);d.rectangle((65,1030,835,1122),fill=C['rose']);text(d,(95,1063),'MECHAS  ·  COR  ·  CUIDADO',26,'paper',800)
im.save(assets/'catalogo-01.png',optimize=True)

im,d=base(2,'Conheça nosso jeito de cuidar')
text(d,(65,135),'Cuidado que começa\nna escuta.',51,'ink',900,spacing=8)
photo_at(im,(65,320,360,520));d=ImageDraw.Draw(im)
text(d,(465,350),'SEU NOME',30,'rose',800)
text(d,(465,405),'Cabeleireira e\nespecialista na\nbeleza de cada\ncliente.',25,'ink',600,spacing=15)
text(d,(465,605),'Apresente aqui sua\nexperiência, seu estilo\ne a proposta do\nseu atendimento.',21,'muted',500,spacing=12)
line(d,895);text(d,(65,935),'Seu espaço. Sua identidade.',29,'ink',800)
text(d,(65,995),'Nome do salão: __________________________\nInstagram: ______________________________\nEndereço: _______________________________',23,'muted',500,spacing=18)
im.save(assets/'catalogo-02.png',optimize=True)

im,d=base(3,'Mechas e coloração sob avaliação')
text(d,(65,140),'MECHAS &\nCOLORAÇÃO',58,'ink',900,spacing=0)
photo_at(im,(65,325,770,380));d=ImageDraw.Draw(im)
label(d,750,'01','Iluminação personalizada','Descreva sua técnica e o resultado proposto.\nInclua o que faz parte do atendimento.')
line(d,900);text(d,(65,940),'ORÇAMENTO SOB AVALIAÇÃO',24,'rose',800)
text(d,(65,1000),'Considere comprimento, histórico e condição\ndos fios para definir o serviço e o orçamento.',23,'muted',500,spacing=15)
im.save(assets/'catalogo-03.png',optimize=True)

im,d=base(4,'Seu menu de cuidados')
text(d,(65,140),'TRATAMENTOS\n& CUIDADOS',55,'ink',900,spacing=4)
d.rounded_rectangle((65,325,835,480),radius=15,fill=C['light']);text(d,(95,355),'Mais cuidado em cada etapa.',31,'ink',800)
text(d,(95,410),'Personalize com os tratamentos do seu salão.',20,'muted',600)
label(d,535,'01','Hidratação','Explique o cuidado oferecido e os itens\ninclusos no seu atendimento.')
line(d,685)
label(d,725,'02','Nutrição','Apresente a proposta do serviço e\nas informações que a cliente precisa saber.')
line(d,875)
label(d,915,'03','Reconstrução','Descreva sua opção de tratamento e\noriente a cliente a solicitar uma avaliação.')
text(d,(65,1110),'VALORES: PREENCHA COM SEUS PREÇOS',18,'rose',800)
im.save(assets/'catalogo-04.png',optimize=True)

im,d=base(5,'Seu menu de cortes e finalização')
text(d,(65,140),'CORTES\n& ESCOVAS',60,'ink',900,spacing=0)
photo_at(im,(465,340,370,650));d=ImageDraw.Draw(im)
text(d,(65,370),'CORTE',32,'rose',900)
text(d,(65,430),'Apresente seu estilo,\no que está incluso\ne as opções para\na sua cliente.',23,'muted',500,spacing=15)
text(d,(65,650),'ESCOVA',32,'rose',900)
text(d,(65,710),'Descreva a finalização\ne informe como\nfunciona o\natendimento.',23,'muted',500,spacing=15)
line(d,1050);text(d,(65,1090),'VALOR DO SERVIÇO: R$ ________',24,'ink',800)
im.save(assets/'catalogo-05.png',optimize=True)

im,d=base(6,'Vamos agendar seu momento?',True)
text(d,(65,145),'SEU PRÓXIMO\nMOMENTO\nDE BELEZA.',62,'paper',900,spacing=0)
d.rounded_rectangle((65,435,835,600),radius=15,fill=C['rose']);text(d,(95,465),'AGENDE SUA AVALIAÇÃO',30,'paper',800)
text(d,(95,525),'WhatsApp: (__) _____-____',28,'paper',600)
text(d,(65,665),'HORÁRIOS DE ATENDIMENTO',23,'light',800)
text(d,(65,725),'Preencha aqui os dias e horários do seu salão.',22,'paper',500)
d.line((65,800,835,800),fill=C['rose'],width=2)
text(d,(65,850),'ANTES DO AGENDAMENTO',23,'light',800)
text(d,(65,905),'• Informe o serviço desejado.\n• Envie referências, se necessário.\n• Confirme data, horário e condições\n  diretamente com a profissional.',23,'paper',500,spacing=18)
im.save(assets/'catalogo-06.png',optimize=True)
# Every preview is exported from the same catalog source used by the website.
(assets/'catalogo-manifest.json').write_text(json.dumps({'status':'base visual para personalização; versão Canva pendente','pages':[f'catalogo-{i:02}.png' for i in range(1,7)]},ensure_ascii=False,indent=2))
