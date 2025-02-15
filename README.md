# EF API

This repository provides sample source code demonstrating the "EF API", which allows external control of "EF digital humans software" and the "digital human" running within it.

Originally designed for internal use, the APIs are currently implemented over "TCP sockets". However, we plan to migrate to an "HTTP(s)" implementation and publish comprehensive API documentation in future releases.

## Prerequisites

### 1. Download the EF Digital Humans Software (Community Edition)
The latest build is available for **Windows and Linux**:  
- [Windows Build](https://github.com/evovor/ef_community/releases/download/v0.1.0-alpha/ef_community_win-v0.1.0-alpha.7z)  
- [Linux Build](https://github.com/evovor/ef_community/releases/download/v0.1.0-alpha/ef_community_linux-v0.1.0-alpha.7z)  

✅ Tested on: Windows 10, 11, and Ubuntu 22.04.  
⚠️ Other operating systems that support **DirectX 11/12** or **Vulkan** might also work.


### 2. Install Python 3  
Ensure you have Python 3 installed:  
- [Python.org](https://www.python.org/downloads/)  
- [Anaconda](https://www.anaconda.com/products/distribution)

### 3. Clone the Repository  
Run the following command to clone the repository:  
```bash
git clone https://github.com/evovor/ef-api.git
```

---

## Running the API Sample

### Step 1: Start the EF Software 
Unzip the EF software and launch it:  

**Windows:**  
```bash
start_ef.bat
```
**Linux:**  
```bash
bash start_ef.sh
```

### Step 2: Run the Sample Code 
For example, to execute the **"speak"** demo:  
```bash
cd ef-api
python speak.py
```
If everything is set up correctly, the digital human should begin speaking.

---

## Future Improvements  
We are actively working on:  
✅ Migrating the API from **TCP to HTTP(s)**.  
✅ Expanding API functionality.  
✅ Publishing comprehensive API documentation.

For feedback, contributions, or issues, please open an [issue](https://github.com/evovor/ef-api/issues) or submit a pull request.