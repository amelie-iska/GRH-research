"""Fail-closed release QA contract; no browser/network/build."""
from pathlib import Path
import json,hashlib,re
HERE=Path(__file__).resolve().parent
GROUPS=json.loads((HERE/"prior-groups-v3.json").read_text())
RUNTIME="c37b2d5d630e794ccfef01ca316385da755622952adae774c4ce569cbdc13d71"
BUILDER="0065a3a1977cd9b1ef1ecd08c6f334d18c9d1375f4c02a6c40ce4c789a6a0f5d"
def validate(e):
 assert e["schema"]=="ramified-release-expectations-v1"
 assert [e["book_pages"],e["math_nodes"],e["tables"],e["frames"]]==[348,10858,389,14]
 assert e["focused_pages"]==[85,243] and e["notes_pages"]==[43,131]
 assert e["global_WS"]=={"idle_timeout_ms":30000,"initial_separate_from_departures":True,"new_fetch_filters":False,"quiet_ms":750}
 for key,base,count in [("prior220_group_names","inherited_group_names",220),("focused_required_group_names","focused_required_group_names",40),("ramified_required_group_names","ramified_required_group_names",44),("lab_required_group_names","lab_required_group_names",58)]:
  assert len(e[key])==len(set(e[key]))==count and set(e[key])==set(GROUPS[base]),key
 assert e["legacy_group_names"] and len(e["legacy_group_names"])==161 and len(e["prior191_group_names"])==191
 assert set(e["legacy_group_names"])<=set(e["prior191_group_names"])<=set(e["prior220_group_names"])
 assert e["required_lab_layouts"]==54 and e["required_saved_strings"]==1218 and e["required_rendered_cells"]==3654
 assert e["assets"]["/public-base.js"]==RUNTIME and e["preserved_public_builder_sha256"]==BUILDER
 assert len(e["prior31_svg_srcs"])==31 and len(e["bundle_svg_srcs"])==32 and e["bundle_svg_srcs"][:31]==e["prior31_svg_srcs"]
 assert len(e["bundle_iframe_srcs"])==14 and e["bundle_iframe_srcs"]==e["prior_bundle_iframe_srcs"]
 assert [e["rg"][x] for x in ["math_nodes","math_nodes_added","old_literal_math_subtrees","old_svg_refs","svg_refs","tables","canonical_labs"]]==[10858,559,10299,31,32,389,14]
 assert len(e["rg"]["labels"])==len(set(e["rg"]["labels"]))==75
 assert e["rg"]["old_math_byte_identical"] and e["rg"]["old_HTML_restored_exactly"]
 assert e["rg"]["old_literal_math_sha256"]==e["old10299_literal_math_sha256"]
 assert e["rg"]["prior31_svg_srcs"]==e["prior31_svg_srcs"]
 assert e["gtl"]["math_nodes"]==10858 and e["gtl"]["math_nodes_added"]==489 and e["gtl"]["svg_refs"]==32
 assert e["lab"]["module_sha256"]=="094fbfb28a46da943ced6f16ed40207e1fc97a57ff97cd780cc085392999247d"
 assert e["lab"]["payload_sha256"]=="e540ac344bbf3d4d07d1ac9fcb8c5cd336a6195c7130a602567242c33bc73171"
 assert len(e["pdfs"])==5 and sorted(v["pages"] for v in e["pdfs"].values())==[43,85,131,243,348]
 assert e["source_HTTP_fallback"] is False
 return True
def math_nodes(html):return re.findall(r"<math\b[\s\S]*?</math>",html)
def math_sections(html):
 starts=list(re.finditer(r"""<section\b[^>]*\bid=["']ramified-gauss-section["'][^>]*>""",html,re.I))
 assert len(starts)==1,"Exactly one explicit ramified continuation"
 start=starts[0];depth=1;end=None
 for token in re.finditer(r"</?section\b[^>]*>",html[start.end():],re.I):
  depth+=-1 if token.group().startswith("</")else 1
  if depth==0:end=start.end()+token.end();break
 assert end is not None,"Balanced ramified continuation"
 return html[:start.start()]+html[end:],html[start.end():end]
def validate_math_preservation(prior,current):
 a=math_nodes(prior);outside,inside=math_sections(current)
 b=math_nodes(outside);added=math_nodes(inside)
 assert len(a)==len(b)==10299 and len(added)==559 and len(math_nodes(current))==10858 and b==a,"All previous10299 rawMathML outside exact newsection must remain ordered byte-identical"
 return hashlib.sha256("\n".join(a).encode()).hexdigest()
