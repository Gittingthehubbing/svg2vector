# SVG2Vector (Simplified)

A simple toolbox to convert SVG graphics to other vector formats like EMF and PDF.

## 🚀 Quick Start (Installation & Compilation)

### Prerequisites
- **Java JDK 8 or higher** (JDK 17/21 recommended)
- **Apache Maven**

### Build from Source
To compile the project and generate an executable "fat-jar" with all dependencies included:

```bash
mvn clean package
```

The resulting executable will be located at:
`target/svg2vector-2.0.0-jar-with-dependencies.jar`

---

## 🐍 Calling from Python

You can easily call this tool from Python using the `subprocess` module. Below is a helper script to wrap the Java calls.

### Example Python Wrapper (`svg2vector.py`)

```python
import subprocess
import os

JAR_PATH = "target/svg2vector-2.0.0-jar-with-dependencies.jar"

def convert_svg(input_file, target="pdf", output_dir="output", extra_args=None):
    """
    Converts an SVG file using the s2v-fh application.
    """
    if not os.path.exists(JAR_PATH):
        raise FileNotFoundError(f"JAR file not found at {JAR_PATH}. Did you run 'mvn package'?")

    # Commands for the 's2v-fh' application
    cmd = [
        "java",
        # For Java 11+, Batik might need these flags:
        # "--add-opens", "java.desktop/java.awt=ALL-UNNAMED", 
        "-jar", JAR_PATH,
        "s2v-fh",
        "--target", target,
        "--file", input_file,
        "--output-directory", output_dir,
        "--create-directories",
        "--overwrite-existing"
    ]
    
    if extra_args:
        cmd.extend(extra_args)

    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")
    
    return result.returncode

# Usage:
# convert_svg("examples/circle-text.svg", target="pdf")
```

---

## 📂 Example Assets

Check the `examples/` directory for test files:
- `examples/circle-text.svg`: Simple SVG with text and a circle.
- `examples/layered-test.svg`: SVG with Inkscape-style layers.
- `examples/time-interval-based.svgz`: Compressed SVGZ test file.

To test your installation quickly:
```bash
# Convert a simple example to PDF
python svg2vector.py examples/circle-text.svg pdf output

# Convert a layered SVG (this will create multiple files)
python svg2vector.py examples/layered-test.svg pdf output --all-layers
```

---

## ☕ Modern Java Run-times (Java 11, 17, 21+)

The project has been updated to use **Java 11** for compilation and runtime. This provides better compatibility with modern environments while maintaining some support for older systems.

### Recommended Fixes for Modern Java:

1.  **Runtime Flags**: When running the JAR on Java 11+, you might encounter `IllegalAccessError` due to stronger encapsulation of internal APIs (specifically in Batik 1.6). Add the following flag if you see AWT/Graphics errors:
    ```bash
    java --add-opens java.desktop/java.awt=ALL-UNNAMED -jar ...
    ```

2.  **Updating `pom.xml`**:
    The compiler properties in `pom.xml` and `src/bundle/pm/project.properties` have already been updated to `11`.

3.  **Dependencies**:
    Both **Batik (1.6)** and **FreeHEP (2.4)** are quite old. If you experience persistent issues, consider updating Batik to version **1.17** in the `pom.xml`.

---

## 🛠 Usage (CLI)

### Using FreeHEP (`s2v-fh`)
Best for PDF and EMF:
```bash
java -jar target/svg2vector-2.0.0-jar-with-dependencies.jar s2v-fh -t pdf -f input.svg
```

### Using Inkscape (`s2v-is`)
Requires Inkscape to be installed on your system:
```bash
java -jar target/svg2vector-2.0.0-jar-with-dependencies.jar s2v-is -t pdf -f input.svg
```

For more options, run with `--help`:
```bash
java -jar target/svg2vector-2.0.0-jar-with-dependencies.jar s2v-fh --help
```
