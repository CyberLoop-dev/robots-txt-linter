<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#a78bfa&height=180&section=header&text=Robots%20Txt%20Linter&fontSize=42&fontColor=ffffff" alt="Robots Txt Linter banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=a78bfa&center=true&vCenter=true&width=650&lines=Catch%20crawler-rule%20mistakes%20before%20launch." alt="Animated project tagline"/></p>
<p align="center">
<img src="https://img.shields.io/github/license/CyberLoop-dev/robots-txt-linter?style=for-the-badge" alt="License"/>
<img src="https://img.shields.io/github/languages/top/CyberLoop-dev/robots-txt-linter?style=for-the-badge" alt="Top language"/>
<img src="https://img.shields.io/github/stars/CyberLoop-dev/robots-txt-linter?style=for-the-badge" alt="Stars"/>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/robots-txt-linter?style=for-the-badge" alt="Last commit"/>
</p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="Robots Txt Linter illustration"/></p>

## 🚀 Overview

Robots TXT Linter is a dependency-free checker for robots.txt files. It catches structural mistakes and highlights potentially surprising rules before they affect search crawlers.

## ✨ Features

- 🧭 Validate user-agent groups and rule placement
- 🔗 Check sitemap URLs and crawl-delay values
- ⚠️ Flag broad Disallow rules and unknown directives
- 🤖 Use strict mode for CI-friendly exit codes

## 🎬 Demo

~~~bash
python main.py robots.txt --strict
~~~

No hosted service or account is required.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/robots-txt-linter.git
cd robots-txt-linter
python main.py --help
~~~

Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
robots-txt-linter/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working command-line core
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional richer reports
- [ ] 🧰 More edge-case fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#a78bfa,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>
