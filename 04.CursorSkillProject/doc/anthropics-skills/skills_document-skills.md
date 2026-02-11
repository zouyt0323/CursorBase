# 文档处理（document-skills）

共 4 个技能。Word/PDF/PPT/Excel 文档的创建、编辑、转换与处理

---

## docx

**中文名**：Word 文档处理

### 功能

创建、读取、编辑和处理 Word 文档（.docx 文件）。支持格式化功能包括目录、标题、页码、信头等。可提取或重新组织 .docx 文件内容、插入或替换图片、执行查找替换、处理修订和批注、将内容转换为精美的 Word 文档。.docx 本质上是 XML 文件的 ZIP 压缩包，使用 pandoc、LibreOffice 等工具链。

**英文原文**：

"Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\", \"word document\", \".docx\", or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a \"report\", \"memo\", \"letter\", \"template\", or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation."

### 使用领域

文档处理、办公自动化、Word 文档、文件格式转换

### 使用场景

当用户提到「Word 文档」、「.docx」，或请求制作带格式的专业文档（报告、备忘录、信函、模板）时使用。不适用于 PDF、电子表格、Google Docs 或与文档生成无关的编程任务。


> **许可证**：专有软件（Proprietary），仅供参考，详见 LICENSE.txt

---

## pdf

**中文名**：PDF 文档处理

### 功能

处理 PDF 文件的全方位工具集。支持读取/提取文本和表格、合并/拆分 PDF、旋转页面、添加水印、创建新 PDF、填写 PDF 表单、加密/解密、提取图片、以及对扫描 PDF 进行 OCR 使其可搜索。主要使用 Python 的 pypdf 等库，包含 reference.md 和 forms.md 等高级参考。

**英文原文**：

Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

### 使用领域

文档处理、PDF 操作、表单处理、OCR 文字识别

### 使用场景

当用户想对 PDF 文件做任何操作时使用，包括读取、提取、合并、拆分、旋转、加密、填表、OCR 等。只要提到 .pdf 文件或要求生成 PDF，即应使用本技能。


> **许可证**：专有软件（Proprietary），仅供参考，详见 LICENSE.txt

---

## pptx

**中文名**：PPT 演示文稿处理

### 功能

处理 .pptx 文件的全方位工具集。支持创建幻灯片、演示文稿、提案稿；读取、解析或提取文本；编辑、修改或更新现有演示文稿；合并或拆分幻灯片文件；处理模板、布局、演讲备注和批注。包含文本提取（markitdown）、缩略图生成和 XML 解包等功能。

**英文原文**：

"Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill."

### 使用领域

文档处理、演示文稿、PPT 制作、商务报告

### 使用场景

当涉及 .pptx 文件时使用——无论是作为输入、输出还是两者兼有。触发词包括「幻灯片」、「演示文稿」、「提案稿」或引用 .pptx 文件名。


> **许可证**：专有软件（Proprietary），仅供参考，详见 LICENSE.txt

---

## xlsx

**中文名**：Excel 电子表格处理

### 功能

处理电子表格文件（.xlsx、.xlsm、.csv、.tsv）的全方位工具。支持打开、读取、编辑、修复现有文件（添加列、计算公式、格式化、图表、清理数据）；从头或从其他数据源创建新电子表格；在表格文件格式之间转换。财务模型遵循专业规范：颜色约定（蓝色输入、黑色公式、绿色内部链接、红色外部链接、黄色关键假设）和数字格式规范。

**英文原文**：

"Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved."

### 使用领域

数据处理、电子表格、Excel 操作、财务建模

### 使用场景

当电子表格文件（.xlsx、.xlsm、.csv、.tsv）是主要输入或输出时使用。包括读取、编辑、创建电子表格，或清理和重组混乱的表格数据。当用户提到电子表格文件名时触发。不适用于 Word 文档、HTML 报告、独立脚本或数据库流水线。


> **许可证**：专有软件（Proprietary），仅供参考，详见 LICENSE.txt
