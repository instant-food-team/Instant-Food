from pathlib import Path
from xml.sax.saxutils import escape
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "presentations" / "HEALTH_MODULE_PPT_BRIEF.md"
TARGET = ROOT / "docs" / "presentations" / "HEALTH_MODULE_PPT_BRIEF.docx"


def paragraph_xml(text: str) -> str:
    text = escape(text)
    return (
        "<w:p>"
        "<w:r>"
        "<w:t xml:space=\"preserve\">"
        f"{text}"
        "</w:t>"
        "</w:r>"
        "</w:p>"
    )


def build_document_body(lines: list[str]) -> str:
    paragraphs = []
    for raw in lines:
        line = raw.rstrip()
        if not line:
            paragraphs.append(paragraph_xml(""))
            continue
        if line.startswith("# "):
            paragraphs.append(paragraph_xml(line[2:].strip()))
            continue
        if line.startswith("## "):
            paragraphs.append(paragraph_xml(line[3:].strip()))
            continue
        if line.startswith("### "):
            paragraphs.append(paragraph_xml(line[4:].strip()))
            continue
        if line.startswith("- "):
            paragraphs.append(paragraph_xml("• " + line[2:].strip()))
            continue
        paragraphs.append(paragraph_xml(line))
    return "".join(paragraphs)


def build_docx(markdown_text: str) -> bytes:
    body = build_document_body(markdown_text.splitlines())
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""
    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""
    document = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
 xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
 xmlns:v="urn:schemas-microsoft-com:vml"
 xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing"
 xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
 xmlns:w10="urn:schemas-microsoft-com:office:word"
 xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
 xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"
 xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk"
 xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml"
 xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape"
 mc:Ignorable="w14 wp14">
  <w:body>
    {body}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
"""
    out = Path(TARGET)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", rels)
        zf.writestr("word/document.xml", document)
    return out.read_bytes()


if __name__ == "__main__":
    text = SOURCE.read_text(encoding="utf-8")
    build_docx(text)
    print(TARGET)
