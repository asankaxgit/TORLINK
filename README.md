<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Web Links Directory</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 font-sans text-gray-800">
    <div class="container mx-auto p-6 max-w-4xl bg-white shadow-lg rounded-lg my-8">
        <header class="mb-8">
            <h1 class="text-4xl font-bold text-center text-gray-900">Dark Web Links Directory</h1>
        </header>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Overview</h2>
            <p class="text-gray-700 leading-relaxed">
                Dark Web Links Directory is a Python-based tool designed to display a curated list of dark web (.onion) links for <strong>educational and research purposes only</strong>. This tool aggregates publicly available .onion URLs to assist researchers and cybersecurity professionals in studying the structure and content of the dark web.
            </p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Disclaimer</h2>
            <p class="text-gray-700 leading-relaxed">
                This tool is intended strictly for <strong>educational and research purposes</strong>. Accessing or using dark web links may involve legal and ethical risks. Always use this tool within the boundaries of applicable laws and regulations, and access .onion sites exclusively through the Tor Browser for safety and anonymity.
            </p>
            <p class="text-gray-700 leading-relaxed mt-4">
                <strong>Copyright</strong>: &copy; 2025 asankaxgit. All Rights Reserved. This tool and its associated code, documentation, and resources are the intellectual property of asankaxgit. Unauthorized reproduction, distribution, or modification of this tool is prohibited without explicit permission from the copyright holder.
            </p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Features</h2>
            <ul class="list-disc list-inside text-gray-700 leading-relaxed">
                <li><strong>Curated List</strong>: Provides a categorized collection of .onion links, including resources for anonymity tools, marketplaces, and informational sites.</li>
                <li><strong>User-Friendly Output</strong>: Displays links in a visually appealing format using ASCII art and color-coded text for better readability.</li>
                <li><strong>Lightweight</strong>: Simple Python script requiring minimal dependencies.</li>
                <li><strong>Educational Focus</strong>: Designed to support research into dark web ecosystems, cybersecurity, and online anonymity.</li>
            </ul>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Prerequisites</h2>
            <p class="text-gray-700 leading-relaxed">
                To run this tool, you need the following:
            </p>
            <ul class="list-disc list-inside text-gray-700 leading-relaxed mt-2">
                <li><strong>Python 3.x</strong>: Ensure Python is installed on your system.</li>
                <li><strong>Tor Browser</strong>: Required to access .onion links safely.</li>
                <li><strong>Dependencies</strong>:
                    <ul class="list-circle list-inside ml-6">
                        <li><code>figlet</code>: For ASCII art banner (optional, install via system package manager).</li>
                        <li><code>toilet</code>: For additional ASCII text formatting (optional, install via system package manager).</li>
                    </ul>
                </li>
            </ul>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Installing Dependencies</h2>
            <p class="text-gray-700 leading-relaxed">On Debian-based systems (e.g., Ubuntu):</p>
            <pre class="bg-gray-900 text-gray-200 p-4 rounded-lg mt-2">
                <code>
sudo apt update
sudo apt install figlet toilet
                </code>
            </pre>
            <p class="text-gray-700 leading-relaxed mt-4">On Red Hat-based systems (e.g., Fedora):</p>
            <pre class="bg-gray-900 text-gray-200 p-4 rounded-lg mt-2">
                <code>
sudo dnf install figlet toilet
                </code>
            </pre>
            <p class="text-gray-700 leading-relaxed mt-4">On macOS (using Homebrew):</p>
            <pre class="bg-gray-900 text-gray-200 p-4 rounded-lg mt-2">
                <code>
brew install figlet toilet
                </code>
            </pre>
            <p class="text-gray-700 leading-relaxed mt-4">No additional Python libraries are required for the script itself.</p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Installation</h2>
            <ol class="list-decimal list-inside text-gray-700 leading-relaxed">
                <li>Clone the repository:
                    <pre class="bg-gray-900 text-gray-200 p-4 rounded-lg mt-2">
                        <code>
git clone https://github.com/asankaxgit/dark-web-links-directory.git
cd dark-web-links-directory
                        </code>
                    </pre>
                </li>
                <li>Ensure you have Python 3 installed:
                    <pre class="bg-gray-900 text-gray-200 p-4 rounded-lg mt-2">
                        <code>
python3 --version
                        </code>
                    </pre>
                </li>
                <li>(Optional) Install <code>figlet</code> and <code>toilet</code> as described in the Prerequisites section for enhanced visual output.</li>
            </ol>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Usage</h2>
            <p class="text-gray-700 leading-relaxed">
                Run the script to display the list of .onion links:
            </p>
            <pre class="bg-gray-900 text-gray-200 p-4 rounded-lg mt-2">
                <code>
python3 dw.py
                </code>
            </pre>
            <p class="text-gray-700 leading-relaxed mt-4">The script will:</p>
            <ul class="list-disc list-inside text-gray-700 leading-relaxed">
                <li>Clear the terminal screen.</li>
                <li>Display an ASCII art banner with the tool's name and a note indicating it was created by Dark Cyber Weapon.</li>
                <li>Output a disclaimer emphasizing the tool's educational purpose.</li>
                <li>List categorized .onion links for research purposes.</li>
            </ul>
            <p class="text-gray-700 leading-relaxed mt-4">
                <strong>Important</strong>: To access the listed .onion links, you must use the Tor Browser. Do not attempt to access these links through a standard browser, as they are only accessible via the Tor network.
            </p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Example Output</h2>
            <pre class="bg-gray-900 text-gray-200 p-4 rounded-lg">
                <code>
          ____          _ _       
         |  _ \  __ _  | | | ___  
         | | | |/ _` | | | |/ _ \ 
         | |_| | (_| | | | |  __/ 
         |____/ \__,_|_|_|_|\___|

                  TOOL BY DARK CYBER WEAPON>>>

         USE ON TOR BROWSER

DISCLAIMER....>>>THIS SCRIPT ONLY MADE FOR RESEARCHES AND EDUCATIONAL PURPOSES ONLY

http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/ – OnionLinks v3
http://6nhmgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion/ – The Hidden Wiki
...
                </code>
            </pre>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Categories of Links</h2>
            <p class="text-gray-700 leading-relaxed">
                The tool organizes .onion links into the following categories:
            </p>
            <ul class="list-disc list-inside text-gray-700 leading-relaxed mt-2">
                <li><strong>General Dark Web Directories</strong>: Links to Hidden Wiki and similar resources.</li>
                <li><strong>Bitcoin and Anonymity Tools</strong>: Services for anonymous Bitcoin transactions and wallets.</li>
                <li><strong>Marketplaces</strong>: Links to various dark web marketplaces (use with caution and for research only).</li>
                <li><strong>Commercial Services</strong>: Miscellaneous services available on the dark web.</li>
                <li><strong>Other Resources</strong>: Blogs, forums, and privacy-focused tools.</li>
            </ul>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Important Notes</h2>
            <ul class="list-disc list-inside text-gray-700 leading-relaxed">
                <li><strong>Legal and Ethical Use</strong>: This tool is for educational and research purposes only. Misuse of the listed links or engaging in illegal activities is strictly against the tool's intended purpose.</li>
                <li><strong>Tor Browser Requirement</strong>: All .onion links require the Tor Browser to access. Download it from <a href="https://www.torproject.org/" class="text-blue-600 hover:underline">torproject.org</a>.</li>
                <li><strong>Security</strong>: Exercise caution when exploring dark web links, as some sites may contain malicious content or scams. Always prioritize your safety and privacy.</li>
            </ul>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Contributing</h2>
            <p class="text-gray-700 leading-relaxed">
                Contributions are welcome! To contribute:
            </p>
            <ol class="list-decimal list-inside text-gray-700 leading-relaxed mt-2">
                <li>Fork the repository.</li>
                <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
                <li>Make your changes and commit (<code>git commit -m "Add new feature"</code>).</li>
                <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
                <li>Open a pull request.</li>
            </ol>
            <p class="text-gray-700 leading-relaxed mt-4">
                Please ensure all contributions align with the tool's educational and research focus.
            </p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">License</h2>
            <p class="text-gray-700 leading-relaxed">
                &copy; 2025 asankaxgit. All Rights Reserved. This tool and its associated code, documentation, and resources are the intellectual property of asankaxgit. Unauthorized reproduction, distribution, or modification is prohibited without explicit permission from the copyright holder. See the <a href="LICENSE" class="text-blue-600 hover:underline">LICENSE</a> file for details.
            </p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Contact</h2>
            <p class="text-gray-700 leading-relaxed">
                For questions or feedback, please open an issue on the <a href="https://github.com/asankaxgit/dark-web-links-directory" class="text-blue-600 hover:underline">GitHub repository</a> or contact the maintainer at <a href="mailto:your-email@example.com" class="text-blue-600 hover:underline">your-email@example.com</a>.
            </p>
            <p class="text-gray-700 leading-relaxed mt-4">
                <strong>Note</strong>: Replace <code>asankaxgit</code> and <code>your-email@example.com</code> with your actual GitHub username and contact information.
            </p>
        </section>
    </div>
</body>
</html>
