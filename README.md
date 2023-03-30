<h1><b>Project Name</b></h1>


<h2><b>Table of Contents</h2></b>
<b>•	Introduction</b><br>
<b>•	Dataset</b><br>
<b>•	Used Libraries</b><Br>
<b>•	Notebooks in use</b><Br>
<b>•	Data Cleaning and Preprocessing</b><Br>
<b>•	Model Building and Evaluation</b><br>

<h2><b>Introduction</b></h2>
The project aims to use personal data to discover the best machine learning model that can identify the right article category
 
 
 
 
<h2><b>Dataset<h2></b>

<h3><b>Dataset structure:</b></h3>
<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width=624
 style='width:468.0pt;margin-left:-.15pt;border-collapse:collapse'>
 <tr style='height:15.75pt'>
  <td width=624 nowrap colspan=3 valign=bottom style='width:468.0pt;border:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.75pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;text-align:center;
  line-height:normal'><span style='color:black'>Dataset's „National defence
  articles and keywords“ structure</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=143 nowrap valign=bottom style='width:107.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>article_id</span></p>
  </td>
  <td width=85 nowrap valign=bottom style='width:63.65pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>int</span></p>
  </td>
  <td width=396 nowrap valign=bottom style='width:297.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>article id</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=143 nowrap valign=bottom style='width:107.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>keyword_id</span></p>
  </td>
  <td width=85 nowrap valign=bottom style='width:63.65pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>int</span></p>
  </td>
  <td width=396 nowrap valign=bottom style='width:297.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>keyword that belongs to the article id</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=143 nowrap valign=bottom style='width:107.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>keyword_name</span></p>
  </td>
  <td width=85 nowrap valign=bottom style='width:63.65pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>string</span></p>
  </td>
  <td width=396 nowrap valign=bottom style='width:297.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>keyword's what belongs to the article name</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=143 nowrap valign=bottom style='width:107.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>article_title</span></p>
  </td>
  <td width=85 nowrap valign=bottom style='width:63.65pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>string</span></p>
  </td>
  <td width=396 nowrap valign=bottom style='width:297.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>article title</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=143 nowrap valign=bottom style='width:107.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>article_body</span></p>
  </td>
  <td width=85 nowrap valign=bottom style='width:63.65pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>string</span></p>
  </td>
  <td width=396 nowrap valign=bottom style='width:297.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>article text</span></p>
  </td>
 </tr>
 <tr style='height:15.0pt'>
  <td width=143 nowrap valign=bottom style='width:107.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>pubdatetime</span></p>
  </td>
  <td width=85 nowrap valign=bottom style='width:63.65pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>datetime</span></p>
  </td>
  <td width=396 nowrap valign=bottom style='width:297.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal'><span
  style='color:black'>article publish date and time</span></p>
  </td>
 </tr>
</table>
 
keyword_id and keyword_name has 7 unique values and these following amounts of articles in a sample data.:
 
<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=500 valign=top style='width:375.25pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Kariuomenės stiprinimas,
  pratybos                                     </span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>10</span></p>
  </td>
 </tr>
 <tr>
  <td width=500 valign=top style='width:375.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Įsigijimai ir biudžetas                                              
  </span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>10</span></p>
  </td>
 </tr>
 <tr>
  <td width=500 valign=top style='width:375.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Saugumo ir gynybos
  politika                                           </span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>10</span></p>
  </td>
 </tr>
 <tr>
  <td width=500 valign=top style='width:375.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Kibernetinis
  saugumas                                                 </span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>10</span></p>
  </td>
 </tr>
 <tr>
  <td width=500 valign=top style='width:375.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Pilietiškumas ir atsparumas propagandai                               </span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>10</span></p>
  </td>
 </tr>
 <tr>
  <td width=500 valign=top style='width:375.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Incidentai, nelaimės,
  kriminalai                                      </span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>10</span></p>
  </td>
 </tr>
 <tr>
  <td width=500 valign=top style='width:375.25pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal;background:
  white;vertical-align:baseline;word-break:break-all'><span style='font-size:
  12.0pt;color:black'>Kariuomenės pagalba kitoms valstybės institucijoms ir
  gyventojams     </span></p>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>&nbsp;</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>10</span></p>
  </td>
 </tr>
</table>
File example: data/Kam_tema_sample_1<br>
 <p></p>
For my work I used bigger dataset:<br>
 
<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Kariuomenės stiprinimas,
  pratybos                                     </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>3000</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Įsigijimai ir biudžetas                                              
  </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>3000</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Saugumo ir gynybos
  politika                                           </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>3000</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Kibernetinis
  saugumas                                                 </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>3000</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Pilietiškumas ir atsparumas propagandai                               </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>3000</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Incidentai, nelaimės,
  kriminalai                                      </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>3000</span></p>
  </td>
 </tr>
 <tr style='height:18.45pt'>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:18.45pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal;background:
  white;vertical-align:baseline;word-break:break-all'><span style='font-size:
  12.0pt;color:black'>Kariuomenės pagalba kitoms valstybės institucijoms ir
  gyventojams     </span></p>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>&nbsp;</span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:18.45pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>1413</span></p>
  </td>
 </tr>
</table>
File example: data/Kam_tema_3000_1

Later I will use these my categories for train target.

In the share drive there is also data that can be used for small predictions:

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Kariuomenės stiprinimas,
  pratybos                                     </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>5</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Įsigijimai ir
  biudžetas                                               </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>5</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Saugumo ir gynybos
  politika                                           </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>5</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Kibernetinis
  saugumas                                                 </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>5</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Pilietiškumas ir atsparumas
  propagandai                               </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>5</span></p>
  </td>
 </tr>
 <tr>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>Incidentai, nelaimės, kriminalai                                     
  </span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>5</span></p>
  </td>
 </tr>
 <tr style='height:18.45pt'>
  <td width=491 valign=top style='width:368.15pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:18.45pt'>
  <p class=MsoNormal style='margin-bottom:0cm;line-height:normal;background:
  white;vertical-align:baseline;word-break:break-all'><span style='font-size:
  12.0pt;color:black'>Kariuomenės pagalba kitoms valstybės institucijoms ir
  gyventojams     </span></p>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  font-family:"Segoe UI",sans-serif;color:#374151'>&nbsp;</span></p>
  </td>
  <td width=132 valign=top style='width:99.35pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:18.45pt'>
  <p class=MsoNormal style='line-height:normal'><span style='font-size:12.0pt;
  color:black'>5</span></p>
  </td>
 </tr>
</table>
File example: data/Kam_predict_sample_1

<h2></b>Used Libraries</b></h2>

matplotlib<br>
seaborn<br>
googletrans<br>
langdetect<br>
sklearn<br>
pandas<br>
numpy<br>
wordcloud<br>
nltk<br>
spaCy<br>
bs4<br>

<h2></b>Notebooks in use</b></h2>
Data_Science_final_projecy_(spaCy) .ipynb – using spaCy vectorizer for later predictions<br>
Data_Science_final_project (cv and tf-idf).ipynb – using spaCy for lemmatizing and later CountVectorizer and TfidfVectorizer for vectorization and predictions<br>


<h2></b>Data Cleaning and Preprocessing</b></h2>
For data cleaning using these functions: <br>
lower(text)<br>
BeautifulSoup.remove_html_tags(text)<br>
special_char(text)<br>
slice(stop=10000)<br>
langdetect.detect_lang(text)<br>
googletrans.translate_text(text, dest_lang)<br>
remove_stopwords(text)<br>


<b>Before cleaning</b><Br>
![after_cleaning](spacy_vect_images/Not_cleaned_data.png)<Br>
<b>After cleaning</b><br>
![after_cleaning](spacy_vect_images/Cleaned_data.png)<Br>


<h2></b>Model Building and Evaluation</b></h2>

Used 3 vectorizers and 1 lemmatizer:<br>
spaCy lemmatizer -> CountVectorizer<br>
spaCy lemmatizer -> TfidfVectorizer<br>
spaCy vectorizer<br>
Built 3 simple models (Logistic Regression, Random Forest Classifier, Decision Tree Classifier) for each vectorizer<br>

The results each reached:<br>
<b>CountVectorizer-> Logistic Regression</b>
![lr_cv](cv_tfidf_images/lr_prediction_heatmap_cv.png)
<br>
<b>CountVectorizer-> Random Forest Classifier</b>
 ![rf_cv](cv_tfidf_images/rdfprediction_heatmap_cv.png)
<br>
<b>CountVectorizer-> Decision Tree Classifier</b>
  ![dt_cv](cv_tfidf_images/dt_prediction_heatmap_cv.png)
<br>

<b>TfidfVectorizer -> Logistic Regression</b>
  ![lr_tfidf](cv_tfidf_images/lr_prediction_heatmap_tfidf.png)
<br>
<b>TfidfVectorizer -> Random Forest Classifier</b>
  ![rf_tfidf](cv_tfidf_images/rdfprediction_heatmap_tfidf.png)
<br>
<b>TfidfVectorizer -> Decision Tree Classifier</b>
  ![dt_tfidf](cv_tfidf_images/dt_prediction_heatmap_tfidf.png)
<br>
 

<b>spaCy vectorizer-> Logistic Regression</b>
   ![lr_spacy](spacy_vect_images/lr_prediction_heatmap.png)<br>
<b>spaCy vectorizer-> Random Forest Classifier</b>
 ![rf_spacy](spacy_vect_images/rf_prediction_heatmap.png)<br>
<b>spaCy vectorizer-> Decision Tree Classifier</b>
 ![dt_spacy](spacy_vect_images/dt_prediction_heatmap.png)<br>
.

