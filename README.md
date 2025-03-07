# LaTeX Abbreviation Fixer
Quick and dirty script for the boys. Collects all words that are just uppercase letters and makes a data file, you add the definitions to this, then run the script again and it will generate some LaTeX code that works with the `acro` package. [See documentation here](https://nl.mirrors.cicku.me/ctan/macros/latex/contrib/acronym/acronym.pdf)

## Usage
1. Create a virtual environment (or not, may break your OS but maybe you like taking risks)
2. Download repo
3. Install deps
```bash
pip install -r requirements.txt
```
4. Get the path to your `tex` files, you can use the Windows "Copy as path" feature in the context menu. The folder you give will be searched recursively. 
5. Run the script
```bash
python.exe .\src\main.py YOURPATHHERE
```
6. Check in- and output folders in the logs and make sure all `tex` files are included and the output paths are correct before texting me
7. Open `abbreviations.json` and define the acronyms like so, if you leave the value empty, it will not be published to the `tex` result either. 
```json
{
    "ACN": "",
    "AGBACHEX": "",
    "ALL": "",
    "AMK": "Advanced Measurement Kit",
}
```
8. Run the script again with `--make-tex`
```bash
python.exe .\src\main.py --make-tex YOURPATHHERE
```
9. Copy the contents of `abbreviations.tex` somewhere in your `tex` source and replace all occurrences of the *defined* acronyms with `\ac{acronym}` instead.
```tex
\section*{Abbreviations}
\begin{acronym}[TDMA]
	\acro{AMK}{Advanced Measurement Kit}
\end{acronym}
```
10. Include the `acronym` package
```tex
\usepackage{acronym} % Acronyms
```
11. Clear `tex` cache and recompile

`acro` will print the full definition of the acronym for the first occurrence of the `\ac{acronym}` command; E.g. `Advanced Measurement Kit (AMK)`. Any other instance will only print the acronym; E.g. `AMK`. You can configure it to put these in the footnotes as well but I haven't figured it out.

Yes you will have to find and replace the existing acronyms yourself, there is no way in fuck I'm writing any code that allows writing to the tex file. I'm not feeling like losing several hours of work if I forget to commit to git :D

Yea, *make backups*. 

## Help 
```
Cool latex abbreviation finder

usage: Cool latex abbreviation finder [-h] [--make-tex] [--output OUTPUT] folder

Finds abbreviations in a tex workspace so you can make a *list*

positional arguments:
  folder           Path to find text files

options:
  -h, --help       show this help message and exit
  --make-tex       Make a tex file with the abbreviations
  --output OUTPUT  Output path, default is output in this repo

Good luck, bye!
```

---

Arne van Iterson, 2025