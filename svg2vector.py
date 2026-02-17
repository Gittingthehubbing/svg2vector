import subprocess
import os
import sys

# Change this path to where your JAR is located after running 'mvn package'
JAR_PATH = os.path.join(os.path.dirname(__file__), "target", "svg2vector-2.0.0-jar-with-dependencies.jar")

def convert_svg(input_file, target="pdf", output_dir="output", extra_args=None):
    """
    Python wrapper for the SVG2Vector Java tool.
    
    :param input_file: Path to the SVG or SVGZ file to convert.
    :param target: Target format (e.g., pdf, emf, svg, png).
    :param output_dir: Directory where the output will be saved.
    :param extra_args: List of additional arguments (e.g., ["--verbose", "--simulate"]).
    :return: Return code from the Java process.
    """
    
    # Check if JAR exists
    if not os.path.exists(JAR_PATH):
        print(f"Error: JAR file not found at {JAR_PATH}")
        print("Please run 'mvn clean package' first.")
        return 1
        
    # Construct the command
    # For modern Java (11+), we may need the --add-opens flag for Batik
    cmd = [
        "java",
        # Uncomment the following if you encounter AWT/Graphics errors on Java 11+
        # "--add-opens", "java.desktop/java.awt=ALL-UNNAMED",
        "-jar", JAR_PATH,
        "s2v-fh",  # Use the FreeHEP/Batik application
        "--target", target,
        "--file", input_file,
        "--output-directory", output_dir,
        "--create-directories",
        "--overwrite-existing"
    ]
    
    if extra_args:
        cmd.extend(extra_args)
        
    print(f"Running command: {' '.join(cmd)}")
    
    # Start the process
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        
        if stdout:
            print("Output:\n", stdout)
        if stderr:
            print("Error/Warning:\n", stderr)
            
        return process.returncode
    except Exception as e:
        print(f"An error occurred while calling Java: {e}")
        return -1

if __name__ == "__main__":
    # Example usage:
    # python svg2vector.py input.svg [target] [output_dir]
    if len(sys.argv) < 2:
        print("Usage: python svg2vector.py <input_file> [target] [output_dir]")
        sys.exit(1)
        
    file_path = sys.argv[1]
    target_format = sys.argv[2] if len(sys.argv) > 2 else "pdf"
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "output"
    
    ret_code = convert_svg(file_path, target_format, out_dir)
    sys.exit(ret_code)
