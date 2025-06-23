
# IPInfo MCP Server

A Python-based MCP (Model Context Protocol) server that fetches IP address geolocation information using the [ipapi.co](https://ipapi.co/) API. This server exposes a tool to retrieve details such as city, country, latitude, and longitude for a given IP address, integrated with Visual Studio Code and GitHub Copilot.

## Features

- **IP Geolocation**: Retrieve geolocation data for any valid IP address using ipapi.co.
- **MCP Integration**: Built with the Python MCP SDK, compatible with VS Code's GitHub Copilot in Agent Mode.
- **Asynchronous HTTP Requests**: Uses `httpx` for efficient, non-blocking API calls.
- **UV Managed**: Managed with `uv` for fast dependency management and project setup.

## Prerequisites

- Python 3.8 or higher
- [Visual Studio Code](https://code.visualstudio.com/) with Python and GitHub Copilot extensions
- [UV](https://docs.astral.sh/uv/) for package management
- Git for version control
- Optional: ipapi.co API key for higher rate limits (free tier available)

## Setup Instructions

1. **Install Python**:
   - Ensure Python 3 is installed:
     ```bash
     sudo apt install python3-full  # Debian/Ubuntu
     python3 --version
     ```

2. **Clone the Repository**:
   - Clone this repository:
     ```bash
     git clone https://github.com/your-username/ipinfo-mcp-server.git
     cd ipinfo-mcp-server
     ```

3. **Set Up a Virtual Environment**:
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv .venv
     source .venv/bin/venv/bin/activate  # On Windows: .venv\Scripts\activate
     ```

4. **Install UV and Dependencies**:
   - Install `uv` in the virtual environment:
     ```bash
     pip install uv
     ```
   - Initialize the project and install dependencies:
     ```bash
     uv init
     uv add "mcp[cli]" httpx
     ```

5. **Run the Server**:
   - Start the MCP server:
     ```bash
     uv run src/ipinfo_mcp_server/server.py
     ```
   - Open the MCP Inspector at `http://localhost:6274/` to test the `get_ip_info` tool.

## Usage in Visual Studio Code

1. **Configure VS Code**:
   - Open the project in VS Code:
     ```bash
     code .
     ```
   - Enable MCP support in VS Code settings:
     ```json
     {
       "chat.mcp.enabled": true
     }
     ```
   - Create a `.vscode/mcp.json` file:
     ```json
     {
       "servers": {
         "IPInfoServer": {
           "type": "stdio",
           "command": "uv",
           "args": ["run", "src/ipinfo_mcp_server/server.py"]
         }
       }
     }
     ```

2. **Test with GitHub Copilot**:
   - Open the GitHub Copilot Chat panel in VS Code.
   - Enable **Agent Mode**.
   - Use the **Tools** icon to select `get_ip_info`.
   - Enter a prompt like:
     ```
     Get IP information for 8.8.8.8
     ```
   - Expected output:
     ```json
     {
       "ip": "8.8.8.8",
       "city": "Mountain View",
       "region": "California",
       "country_name": "United States",
       "latitude": 37.751,
       "longitude": -97.822,
       ...
     }
     ```

## Project Structure

```
ipinfo-mcp-server/
├── .venv/                # Virtual environment
├── src/
│   └── ipinfo_mcp_server/
│       └── server.py     # MCP server implementation
├── .vscode/
│   └── mcp.json          # VS Code MCP configuration
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── pyproject.toml        # UV project configuration
```

## Optional: Using an ipapi.co API Key

To use an API key for higher rate limits:
1. Sign up at [ipapi.co](https://ipapi.co/) to get a key.
2. Update `.vscode/mcp.json` to include the key:
   ```json
   {
     "inputs": [
       {
         "type": "promptString",
         "id": "ipapi_key",
         "description": "ipapi.co API Key",
         "password": true
       }
     ],
     "servers": {
       "IPInfoServer": {
         "type": "stdio",
         "command": "uv",
         "args": ["run", "src/ipinfo_mcp_server/server.py"],
         "env": {
           "IPAPI_KEY": "${input:ipapi_key}"
         }
       }
     }
   }
   ```
3. Modify `server.py` to use the key (see [server.py](#)).

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## Troubleshooting

- **MCP Server Not Found in VS Code**:
  - Ensure `chat.mcp.enabled` is set in VS Code settings.
  - Verify `.vscode/mcp.json` is correct.
- **ipapi.co API Errors**:
  - Check your internet connection.
  - Ensure the API key is valid if used.
- **UV Installation Issues**:
  - Use a virtual environment or `pipx` to avoid PEP 668 errors:
    ```bash
    pipx install uv
    ```

## License

MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

- [ipapi.co](https://ipapi.co/) for the geolocation API.
- [MCP SDK](https://github.com/xai-org/mcp-python-sdk) for the server framework.
- [UV](https://docs.astral.sh/uv/) for dependency management.
```

---

### **Instructions to Add the README.md**

1. **Create the File**:
   - In your project directory (`~/Desktop/MCP_server`):
     ```bash
     touch README.md
     ```
   - Open `README.md` in VS Code:
     ```bash
     code README.md
     ```
   - Copy and paste the above Markdown content.

2. **Replace `your-username`**:
   - Update the `git clone` URL in the README to match your GitHub username:
     ```markdown
     git clone https://github.com/niraj-ghetita/ipinfo-mcp-server.git
     ```

3. **Add a License File** (Optional):
   - Create a `LICENSE` file for the MIT License:
     ```bash
     touch LICENSE
     ```
   - Add the MIT License text (available from [choosealicense.com](https://choosealicense.com/licenses/mit/)):
     ```
     MIT License

     Copyright (c) 2025 Niraj Ghetita

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the "Software"), to deal
     in the Software without restriction, including without limitation the rights
     to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
     copies of the Software, and to permit persons to whom the Software is
     furnished to do so, subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
     SOFTWARE.
     ```

4. **Commit and Push to GitHub**:
   - Stage and commit the `README.md` (and `LICENSE` if created):
     ```bash
     git add README.md LICENSE
     git commit -m "Add README and LICENSE files"
     ```
   - Push to your GitHub repository:
     ```bash
     git push origin main
     ```

---

### **Notes**
- **Customize the README**: Update the "Acknowledgments" or add sections like "Roadmap" if you plan to extend the project.
- **Ensure Project Structure**: The README assumes the project structure matches the earlier setup (e.g., `src/ipinfo_mcp_server/server.py`). If your directory differs, adjust the paths in the README.
- **Test Links**: After pushing to GitHub, verify that links (e.g., to `LICENSE`) work correctly.
- **Virtual Environment**: The README includes instructions for the virtual environment setup to address your earlier PEP 668 error.

If you need help with additional sections for the README, tweaks to the content, or further setup steps, let me know!