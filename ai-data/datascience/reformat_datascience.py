#!/usr/bin/env python3
"""
Reformat pandoc-generated HTML files in the datascience folder to use
the blog's standard Monochromed layout.
"""

import re
import os
import sys

DATASCIENCE_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = [
    "Assigment2FineParticulate.html",
    "Basic_Inferential_Data.html",
    "Curso_2_R_Programming.html",
    "Curso_3_Getting_and_Cleaning_Data.html",
    "Curso_4_Exploratory_Data_Analysis.html",
    "Curso_5_Reproducible_research.html",
    "Curso_6.html",
    "Curso_6_Statistical_Inference.html",
    "Curso_6_Statistical_InferenceCopy.html",
    "Curso_7_Regression_Models.html",
    "Dplyr2.html",
    "ElectricPowerConsumptionAssigment1.html",
    "Extra3_Datascrapping.html",
    "Extra3_FHIR.html",
    "Extra3_bbdd.html",
    "HospitalQuality.html",
    "PA1_template.html",
    "PollutionData.html",
    "Simultion_Example.html",
    "SmartphoneSensor.html",
    "cacheObjects.html",
    "dplyr.html",
    "pollutantAssignment1.html",
    "run_analysis.html",
    "tidyr.html",
]

TEMPLATE = """\
<!DOCTYPE HTML>
<!--
\tMonochromed by TEMPLATED
-->
<html>
<head>
  <title>{title} - Blog de Miguel Angel Huerta</title>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <meta name="description" content="" />
  <meta name="keywords" content="" />
  <link href='http://fonts.googleapis.com/css?family=Oxygen:400,300,700' rel='stylesheet' type='text/css'>
  <!--[if lte IE 8]><script src="../../js/html5shiv.js"></script><![endif]-->
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
  <script src="../../js/skel.min.js"></script>
  <script src="../../js/skel-panels.min.js"></script>
  <script src="../../js/init-subfolder-datascience.js"></script>
  <noscript>
    <link rel="stylesheet" href="../../css/skel-noscript.css" />
    <link rel="stylesheet" href="../../css/style.css" />
  </noscript>
  <!--[if lte IE 8]><link rel="stylesheet" href="../../css/ie/v8.css" /><![endif]-->
  <!--[if lte IE 9]><link rel="stylesheet" href="../../css/ie/v9.css" /><![endif]-->
</head>
<body>
  <!-- Header -->
  <div id="header">
    <div class="container">
      <div id="logo">
        <h1><a href="../../index.html">Blog de Miguel Angel Huerta</a></h1>
        <span>Design by TEMPLATED</span>
      </div>
      <nav id="nav">
        <ul>
          <li><a href="../../index.html">Homepage</a></li>
          <li><a href="../../hardware-projects/index.html">Proyectos con Dispositivos</a></li>
          <li><a href="../../software-projects/index.html">Proyectos de Software</a></li>
          <li class="active"><a href="../index.html">IA &amp; Data</a></li>
          <li><a href="../../vida/index.html">Vida</a></li>
        </ul>
      </nav>
    </div>
  </div>
  <!-- Main -->
  <div id="main">
    <div class="container">
      <div class="row">
        <!-- Sidebar -->
        <div id="sidebar" class="4u">
          <section>
            <header><h2>Data Science</h2></header>
            <ul class="default">
              <li><a href="../data-science.html#maths">Maths</a></li>
              <li><a href="../data-science.html#lifecycle">Data Science life cycle</a></li>
              <li><a href="../data-science.html#tabular-data">Tabular Data</a></li>
              <li><a href="../data-science.html#johns-hopkins">Johns Hopkins</a></li>
            </ul>
          </section>
          <section>
            <header><h2>Otras secciones</h2></header>
            <ul class="default">
              <li><a href="../data.html">Data</a></li>
              <li><a href="../machine-learning.html">Machine Learning &amp; IA</a></li>
              <li><a href="../estilos.html">Software Engineer</a></li>
              <li><a href="https://github.com/mahdsip/DataScience">GitHub</a></li>
            </ul>
          </section>
        </div>
        <!-- Content -->
        <div id="content" class="8u skel-cell-important">
          <section>
            <header>
              <h2>{title}</h2>
            </header>
            {body_content}
          </section>
        </div>
      </div>
    </div>
  </div>
  <!-- Footer -->
  <div id="footer">
    <div class="container">
      <div class="row">
        <div class="3u">
          <section>
            <ul class="style1">
              <li><img src="../../images/pics05.jpg" width="78" height="78" alt="">
                <p>Proyecto KDE </p>
                <a href="https://www.kde.org/">kde.org</a>
                <p class="posted">August 11, 2014  |  (10 )  Comments</p>
              </li>
            </ul>
          </section>
        </div>
        <div class="3u">
          <section>
            <ul class="style1">
              <li class="first"><img src="../../images/debian.jpg" width="78" height="78" alt="">
                <p>Debian</p>
                <a href="https://www.debian.org/index.es.html">debian</a>
                <p class="posted">August 11, 2014  |  (10 )  Comments</p>
              </li>
            </ul>
          </section>
        </div>
        <div class="6u">
          <section>
            <header><h2>Informacion de contacto</h2></header>
            <p>mahdsip@gmail.com</p>
            <ul class="default">
              <li><a href="https://github.com/mahdsip">Perfil de github</a></li>
              <li><a href="https://www.swe.siemens.com/spain/web/es/healthcare/med_innova/Pages/amivital.aspx">Proyecto AmiVital</a></li>
              <li><a href="http://www.oasis-project.eu/">Proyecto OASIS</a></li>
              <li><a href="http://www.fiware.org/">Proyecto Fiware</a></li>
            </ul>
          </section>
        </div>
      </div>
    </div>
  </div>
  <!-- Copyright -->
  <div id="copyright">
    <div class="container">
      Design: <a href="http://templated.co">TEMPLATED</a> Images: <a href="http://unsplash.com">Unsplash</a> (<a href="http://unsplash.com/cc0">CC0</a>)
    </div>
  </div>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-134684500-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'UA-134684500-1');
  </script>
</body>
</html>
"""


def read_file(path):
    """Read file with UTF-8, fall back to latin-1."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='latin-1') as f:
            return f.read()


def extract_title(content):
    """Extract page title from <title> tag."""
    m = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return "Data Science"


def extract_body(content):
    """Extract everything between the opening <body...> and closing </body>."""
    # Match opening body tag (may have attributes), capture everything until </body>
    m = re.search(r'<body[^>]*>(.*)</body>', content, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1)
    # Fallback: return all content if no body tags found
    return content


def process_file(filepath):
    """Process a single HTML file, overwriting with the new template."""
    content = read_file(filepath)
    title = extract_title(content)
    body_content = extract_body(content)
    new_html = TEMPLATE.format(title=title, body_content=body_content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    return title


def verify_file(filepath):
    """
    Verify the file contains required markers and does NOT contain
    large base64 blobs in the head section.
    Returns a dict of check -> bool.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()

    # Extract <head> section for negative checks
    head_match = re.search(r'<head[^>]*>(.*?)</head>', content, re.IGNORECASE | re.DOTALL)
    head_content = head_match.group(1) if head_match else ""

    checks = {
        'has_skel_min_js':    'skel.min.js' in content,
        'has_id_header':      'id="header"' in content,
        'has_id_footer':      'id="footer"' in content,
        'has_id_content':     'id="content"' in content,
        'no_font_base64_in_head':     'data:application/font' not in head_content,
        'no_png_base64_in_head':      'data:image/png;base64,iVBORw0KGgo' not in head_content,
    }
    return checks


def main():
    results = {}
    print("=" * 70)
    print("Processing files...")
    print("=" * 70)

    for filename in FILES:
        filepath = os.path.join(DATASCIENCE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  MISSING: {filename}")
            results[filename] = None
            continue
        title = process_file(filepath)
        print(f"  Processed: {filename}  (title: {title!r})")
        results[filename] = verify_file(filepath)

    print()
    print("=" * 70)
    print("Verification results:")
    print("=" * 70)

    all_pass = True
    for filename in FILES:
        checks = results.get(filename)
        if checks is None:
            print(f"  {filename}: FILE MISSING")
            all_pass = False
            continue

        passed = all(checks.values())
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_pass = False
        failed_checks = [k for k, v in checks.items() if not v]
        if failed_checks:
            print(f"  [{status}] {filename}")
            for c in failed_checks:
                print(f"         FAILED: {c}")
        else:
            print(f"  [{status}] {filename}")

    print()
    if all_pass:
        print("All files passed verification.")
    else:
        print("Some files FAILED verification. See above.")
        sys.exit(1)


if __name__ == '__main__':
    main()
