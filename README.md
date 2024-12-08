# Digital-Logic-Design

This repository contains a comprehensive collection of resources, assignments, projects, and code implementations for the **Digital Logic Design** course. The materials are structured to facilitate learning about digital design concepts, hardware description languages, assembly programming, and computer architecture.

## 📁 Repository Structure

### 1. **Assembler Project**
   - **`Assembler.py`**: A Python program implementing an assembler for the Hack computer architecture.
   - **`Project (Design of Hack Assembler).pdf`**: Documentation and design details of the Hack assembler project.

### 2. **Assignments**
   - **`DLD-Assignment-01.pdf`** & **`DLD-Assignment-02.pdf`**: Problem sets exploring digital logic design concepts.
   - Various image files containing solutions and explanations for the assignments.

### 3. **Data Logic Design Lab**
   - Lab manuals and practical exercises, including:
     - **`LAB 10 Subtractors.pdf`**
     - **`LAB 11+12 Decoders and Encoders.pdf`**
     - Supporting images and diagrams for the lab work.

### 4. **Important Books and Lectures**
   - **`Digital Design Global Edition by M. Morris Mano, Michael Ciletti.pdf`**: Reference textbook.
   - **COAL_VLecs-master.zip**: Collection of lecture codes, tutorials, and reference materials, including HDL and assembly language examples.

### 5. **Lecture Slides**
   - Comprehensive lecture slides covering key topics like:
     - Simplification of Boolean Circuits
     - Arithmetic Circuits
     - Decoders, Encoders, Mux, and DMux
     - Design of ALU, Registers, and Memory
     - Instruction Set Architecture and Hack Machine Language

### 6. **Images**
   - Diagrams and hierarchical illustrations, such as:
     - **`Hirearchy of classes.png`**
     - **`memory hirearchy.JPG`**
     - Boolean expressions like maxterms and minterms.

### 7. **Tools**
   - Scripts and executables for hardware simulation and assembly programming, including:
     - **`Assembler.bat`**, **`Assembler.sh`**
     - **`CPUEmulator.bat`**, **`HardwareSimulator.sh`**
     - **Built-in VM code and chip definitions**

### 8. **HDL Programs for Hack Computer**
These programs define the essential components of the Hack computer. Each HDL file describes a specific hardware component, using the HDL syntax supported by the Hack hardware simulator.

#### **1. Arithmetic and Logical Components**
- **`Add16.hdl`**: 16-bit adder.
- **`FullAdder.hdl`**: Combines basic logic gates to perform full addition of bits.
- **`HalfAdder.hdl`**: Basic half-adder implementation.
- **`ALU.hdl`**: Arithmetic Logic Unit implementation, supporting basic arithmetic and logical operations.

#### **2. Multiplexers and Demultiplexers**
- **`Mux.hdl`**: Basic multiplexer (2-input).
- **`Mux16.hdl`**: 16-bit multiplexer.
- **`Mux4Way16.hdl`**: 4-way multiplexer for 16-bit inputs.
- **`Mux8Way16.hdl`**: 8-way multiplexer for 16-bit inputs.
- **`DMux.hdl`**: Basic demultiplexer.
- **`DMux4Way.hdl`**: 4-way demultiplexer.
- **`DMux8Way.hdl`**: 8-way demultiplexer.

#### **3. Memory Components**
- **`Bit.hdl`**: Basic memory element to store a single bit.
- **`Register.hdl`**: 16-bit register for data storage.
- **`RAM8.hdl`**: 8-word RAM.
- **`RAM64.hdl`**: 64-word RAM.
- **`RAM512.hdl`**: 512-word RAM.
- **`RAM4K.hdl`**: 4K-word RAM.
- **`RAM16K.hdl`**: 16K-word RAM.
- **`PC.hdl`**: Program Counter, which keeps track of the instruction address.

#### **4. Control and Computation Components**
- **`CPU.hdl`**: The central processing unit of the Hack computer, integrating the ALU, registers, and control logic.
- **`Memory.hdl`**: Combines RAM and other storage components to create the main memory.
- **`Computer.hdl`**: The top-level module of the Hack computer, integrating the CPU, memory, and input/output control.

#### **5. Logic Gates**
- **`And.hdl`**, **`Or.hdl`**, **`Xor.hdl`**, **`Not.hdl`**, **`Nand.hdl`**: Basic gates implemented using HDL.
- **`And16.hdl`**, **`Or16.hdl`**, **`Not16.hdl`**: 16-bit versions of the basic gates.

---

### **How to Use**
1. **Install Hack Simulator**: Use the tools provided in your repository, such as `HardwareSimulator.bat` or `HardwareSimulator.sh`, to test HDL files.
2. **Run the HDL Programs**:
   - Open the `HardwareSimulator`.
   - Load an HDL file (e.g., `CPU.hdl`).
   - Run tests using the provided `.tst` and `.cmp` files.

These HDL programs provide a complete implementation of the Hack computer and are perfect for learning computer architecture and hardware design principles.
## 🚀 Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Digital-Logic-Design.git
   cd Digital-Logic-Design
   ```

2. **Run the Assembler**:
   Navigate to the `Assembler Project` directory and execute:
   ```bash
   python Assembler.py
   ```

3. **Explore the Lecture Codes**:
   Open HDL files or assembly codes using a text editor or simulation tools provided in the `tools` directory.

## 🛠️ Features

- **Assembler Implementation**: Converts Hack assembly code to binary machine code.
- **HDL Designs**: Complete set of hardware description language files for digital circuit simulations.
- **Instruction Set Architecture**: Examples of low-level programming for the Hack computer.
- **Comprehensive Resources**: Includes assignments, lecture slides, and reference materials.

## 🤝 Contributions

Contributions, suggestions, and feedback are welcome! Please create a pull request or open an issue to improve the repository.
