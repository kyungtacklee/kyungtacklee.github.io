from pathlib import Path
import re, argparse
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, HRFlowable, PageBreak, Spacer

def build(source,output):
 navy=colors.HexColor('#17324D'); accent=colors.HexColor('#5B5BD6'); dark=colors.HexColor('#20262E'); muted=colors.HexColor('#56616D')
 def style(name,size,leading,**kw):return ParagraphStyle(name,fontName=kw.pop('fontName','Helvetica'),fontSize=size,leading=leading,textColor=dark,**kw)
 normal=style('body',9.4,12.2,spaceAfter=3)
 bullet=style('bullet',9.2,12,leftIndent=12,firstLineIndent=-8,spaceAfter=2)
 small=style('small',8.7,11.3,leftIndent=12,firstLineIndent=-8,spaceAfter=2)
 heading=style('section',11,13,fontName='Helvetica-Bold',spaceBefore=8,spaceAfter=4,keepWithNext=True)
 heading.textColor=navy
 entry=style('entry',9.7,12,fontName='Helvetica-Bold',spaceBefore=5,spaceAfter=3,keepWithNext=True)
 date=style('date',8.5,11,fontName='Helvetica-Bold',alignment=2);date.textColor=muted
 name=style('name',22,25,spaceAfter=6);name.textColor=navy
 tag=style('tag',10,12,fontName='Helvetica-Bold',spaceAfter=4);tag.textColor=accent
 contact=style('contact',8.3,11,spaceAfter=3);contact.textColor=muted
 def rich(t):
  parts=re.split(r'\*\*',t)
  return ''.join(('<b>'+escape(x)+'</b>') if i%2 else escape(x) for i,x in enumerate(parts))
 lines=Path(source).read_text().splitlines();story=[];sect='';intro=0
 for raw in lines:
  line=raw.strip()
  if not line or line.startswith('<!--'):continue
  if line.startswith('# '):story.append(Paragraph(rich(line[2:]),name));intro=1
  elif line.startswith('## '):
   sect=line[3:]
   if sect in ['SELECTED PROJECTS','EDUCATION']:story.append(PageBreak())
   story.extend([Paragraph(rich(sect),heading),HRFlowable(width='100%',thickness=.75,color=accent,spaceAfter=4)])
  elif line.startswith('### '):
   t=line[4:];parts=t.rsplit(' | ',1)
   if len(parts)==2 and re.match(r'\d{4}',parts[1]):
    tab=Table([[Paragraph(rich(parts[0]),entry),Paragraph(rich(parts[1]),date)]],colWidths=[143*mm,35*mm])
    tab.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),2)]));tab.keepWithNext=True;story.append(tab)
   else:story.append(Paragraph(rich(t),entry))
  elif not sect and intro:
   story.append(Paragraph(rich(line),tag if intro==1 else contact));intro+=1
  elif line.startswith('- '):
   sty=small if sect in ['SELECTED HONORS','SELECTED PUBLICATIONS & PATENTS'] else bullet
   if raw.startswith('  '):
    sty=ParagraphStyle('nested',parent=sty,leftIndent=22,firstLineIndent=-8)
   p=Paragraph('&#8226; '+rich(line[2:]),sty)
   if line.endswith(':'):p.keepWithNext=True
   story.append(p)
  else:story.append(Paragraph(rich(line),normal))
 def footer(c,d):
  c.setStrokeColor(colors.HexColor('#D8DEE5'));c.setLineWidth(.4);c.line(16*mm,16*mm,A4[0]-16*mm,16*mm)
  c.setFont('Helvetica',7.5);c.setFillColor(muted);c.drawString(16*mm,12*mm,'Kyungtack Lee | Resume');c.drawCentredString(A4[0]/2,12*mm,f'Page {d.page}')
 doc=SimpleDocTemplate(str(output),pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=13*mm,bottomMargin=22*mm,title='Kyungtack Lee Resume',author='Kyungtack Lee')
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('output');args=p.parse_args();build(args.source,args.output)
