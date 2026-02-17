# SVG2Vector (Simplified)

A simple toolbox to convert SVG graphics to other vector formats like EMF and PDF.

## Quick Start (Installation & Compilation)

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

## Example Assets

Check the `examples/` directory for test files:
- `examples/circle-text.svg`: Simple SVG with text and a circle.
- `examples/layered-test.svg`: SVG with Inkscape-style layers.
- `examples/time-interval-based.svgz`: Compressed SVGZ test file.

---

## Modern Java Run-times (Java 11, 17, 21+)

The project has been auto-updated to use **Java 11** for compilation and runtime. This provides better compatibility with modern environments while maintaining some support for older systems.

---

## Usage (CLI)

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
