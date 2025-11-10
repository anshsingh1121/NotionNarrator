# Biomedical Signal Processing: Resting Potential

## 1. Key Definitions

*   **Resting Potential:** The electrical charge difference across the plasma membrane of a cell when it is in a non-excited state, or at rest. It is the charge associated with a resting cell.
*   **Action Potential:** A rapid, temporary change in the membrane potential of a cell, which is used for communication between cells, such as neurons and muscle cells.

## 2. The Cellular Environment

The resting potential is established by the interaction between the cell's membrane, various ion channels, and the differing ion concentrations inside and outside the cell.

<img src="images/0/image_1.png" alt="Diagram of a cell showing key components for establishing membrane potential." width="400"/>

### Components:

*   **Cell Membrane:** A lipid bilayer that separates the intracellular fluid from the extracellular fluid. It is selectively permeable to ions.
*   **Intracellular Fluid (ICF):** The fluid within the cell. It has a high concentration of potassium (K+) ions and low concentration of sodium (Na+) ions.
*   **Extracellular Fluid (ECF):** The fluid outside the cell. It has a high concentration of Na+, Chloride (Cl-), and Calcium (Ca2+) ions, and a low concentration of K+ ions.
*   **Ion Channels & Pumps:**
    *   **Leaky K+ Channel:** An uncontrolled, passive channel that is always open, allowing K+ ions to move across the membrane according to their concentration gradient.
    *   **Voltage-Gated Na+ Channel:** A channel that opens and closes in response to changes in membrane voltage. It is crucial for generating action potentials.
    *   **Sodium-Potassium Pump (Na+/K+ ATPase):** An active transport mechanism that pumps 3 Na+ ions out of the cell for every 2 K+ ions it pumps in. This process requires energy.

## 3. The Role of ATP (Adenosine Triphosphate)

The Na+/K+ pump is powered by ATP, the primary energy currency of the cell.

*   **Hydrolysis:** The pump uses the energy released from the hydrolysis of ATP.
    *   ``ATP + H₂O → ADP + Pᵢ + Energy``
*   **(Note:** The notes state ATP is made in the nucleus. While the nucleus directs protein synthesis, ATP is primarily synthesized in the mitochondria through cellular respiration.)

## 4. Examples of Resting Potential (R.P.) in Different Cells

The resting potential varies depending on the cell type:

*   **Skeletal Muscle:** -90mV
*   **Neuron Cell:** -60mV
*   **Smooth Muscle Cell:** -60mV
*   **Cardiac Cell:** ≈ -50mV to -90mV
*   **Cartilage:** -8mV
*   **Red Blood Cell (RBC):** -8.4mV

## 5. Establishment of the Resting Potential in a Neuron (-60mV)

The resting potential is primarily established by the outward diffusion of K+ ions through leaky K+ channels.

### Step 1: K+ Concentration Gradient
There is a high concentration of K+ inside the cell (e.g., 140 mmole/lt) and a low concentration outside (e.g., 4 mmole/lt). This chemical gradient drives K+ ions to move out of the cell.

<img src="images/0/image_2.png" alt="Diagram showing the K+ concentration gradient across a cell membrane with a leaky K+ channel." width="400"/>

### Step 2: K+ Efflux and Charge Separation
As positively charged K+ ions (cations) diffuse out of the cell through the leaky channels, they leave behind a net negative charge inside the cell. This creates an electrical gradient.


<img src="images/0/image_3.png" alt="Diagram showing how K+ diffusion creates a net negative charge inside the cell, which opposes further K+ efflux." width="400"/>


### Step 3: Electrochemical Equilibrium

The outward movement of K+ ions makes the inside of the cell progressively more negative (e.g., -5mV, -10mV...). This internal negativity creates an electrical force that pulls the positive K+ ions back into the cell.

The efflux of K+ continues until the outward force from the concentration gradient is perfectly balanced by the inward electrical force. This point of equilibrium is the **resting membrane potential**. For a neuron, this value is approximately **-60mV**.

---
# Ion Channels and Cellular Membrane Potentials

This document outlines the fundamental principles governing ion movement across a cell membrane, focusing on voltage-gated sodium channels, electrochemical gradients, and the equilibrium potentials of key ions. These concepts are crucial in fields like neurobiology and biomedical engineering for understanding nerve impulses and cellular communication.

## 1. Voltage-Gated Sodium (Na⁺) Channels

A **Voltage-Gated Sodium Channel** is a type of transmembrane protein that forms an ion channel pore, allowing sodium ions (Na⁺) to pass through the cell membrane. As the name implies, the channel's permeability to Na⁺ is regulated by the membrane potential (voltage) across it.

These channels play a critical role in the initiation and propagation of action potentials in excitable cells like neurons. The notes indicate a key feature: the gate is **closed** when the membrane potential is below a certain threshold, such as at a resting potential of -60mV.

![A diagram illustrating a voltage-gated sodium channel in a cell membrane.](images/1/image_1.png)

The diagram also depicts the **Na⁺/K⁺-ATPase pump**, an active transport mechanism that uses ATP to move sodium ions out of the cell against their concentration gradient. This pump is essential for maintaining the low intracellular Na⁺ concentration required for the electrochemical gradient.

## 2. Electrochemical Gradients

The movement of an ion across a membrane is governed by its **electrochemical gradient**, which is the sum of two distinct forces:

*   **Concentration Gradient:** The force driving ions to move from an area of higher concentration to an area of lower concentration.
*   **Electrical Gradient (Membrane Potential):** The force exerted on an ion due to the difference in electrical charge across the membrane. Positively charged ions (cations) are attracted to the negatively charged side of the membrane, and vice-versa for anions.

The net driving force, or **Electrochemical Force (ECF)**, determines the direction and magnitude of ion flow when a channel is open.

![A schematic of the electrochemical forces acting on Sodium ions.](images/1/image_2.png)

For sodium (Na⁺), both the concentration gradient (much higher outside the cell) and the electrical gradient (negative inside the cell) typically push it into the cell, creating a strong inward electrochemical force.

## 3. Typical Ion Concentrations and Equilibrium Potentials

The table below lists the typical concentrations of several important ions in the **Intracellular Fluid (ICF)** and **Extracellular Fluid (ECF)**, along with their respective equilibrium potentials.

| Ion              | Intracellular Fluid Conc. | Extracellular Fluid Conc. | Equilibrium Potential (E_ion) |
|-------------------|---------------------------|---------------------------|-------------------------------|
| **Na⁺** (Sodium)  | 15 mM/L                   | 145 mM/L                  | +60.6 mV                      |
| **K⁺** (Potassium)| 150 mM/L                  | 4 mM/L                    | -96 mV                        |
| **Ca²⁺** (Calcium)| 70 nM/L                   | 2 mM/L                    | +137 mV                       |
| **Cl⁻** (Chloride)| 10 mM/L                   | 110 mM/L                  | -64.05 mV                     |
| **Mg²⁺** (Magnesium)| 0.5 mM/L                  | 1 mM/L                    | +9.26 mV                      |

### Equilibrium Potential

The **Equilibrium Potential** (or *Nernst Potential*) for a given ion is the specific membrane voltage at which the electrical gradient perfectly balances the concentration gradient. At this potential, there is no net movement of that ion across the membrane, even if its channels are open. It is calculated using the Nernst equation and is fundamental to determining a cell's overall resting membrane potential.

---

# Excitable Cell Physiology: Membrane Potentials

This document covers the fundamental equations and concepts used to describe the electrical potential across the membrane of excitable cells, such as neurons and muscle cells.

## Relative Permeability of Ions

The cell membrane is selectively permeable to different ions. The relative permeability describes how easily a specific ion can cross the membrane compared to other ions. In a typical resting neuron, the membrane is most permeable to potassium (K⁺).

*   **Potassium (K⁺):** The permeability is set as the baseline reference. `P_K⁺ = 1`
*   **Sodium (Na⁺):** The membrane is much less permeable to sodium. `P_Na⁺ = 0.03 * P_K⁺`
*   **Chloride (Cl⁻):** Chloride permeability is also relatively low compared to potassium. `P_Cl⁻ ≈ 0.1 * P_K⁺`

This high resting permeability to K⁺ is a primary reason why the resting membrane potential is close to the K⁺ equilibrium potential.

## Goldman-Hodgkin-Katz (GHK) Equation

While the Nernst potential calculates the equilibrium for a single ion, the Goldman-Hodgkin-Katz (GHK) equation is used to calculate the overall **Resting Membrane Potential (RMP)** of a cell. It considers the contributions of all major ions, weighted by their relative permeability.

### Formula

The equation, as noted, is a simplified form often used in physiology:

`RMP (V_rest) = -60mV * log₁₀ [ (P_K[K⁺]_out + P_Na[Na⁺]_out + P_Cl[Cl⁻]_out) / (P_K[K⁺]_in + P_Na[Na⁺]_in + P_Cl[Cl⁻]_in) ]`

*   `V_rest` is the resting membrane potential.
*   `P_ion` is the relative permeability of a specific ion (e.g., `P_K`).
*   `[ion]_out` and `[ion]_in` are the concentrations of the ion outside and inside the cell, respectively.

*Note: In the standard GHK equation, the concentration terms for anions (like Cl⁻) are inverted (`[Cl⁻]_in / [Cl⁻]_out`) compared to cations to correctly account for their negative charge. The version in the notes simplifies this but may require careful application.* 

## Nernst Potential

The **Nernst Potential**, also known as the **Equilibrium Potential**, is the theoretical membrane potential at which the net flow of a *single, specific ion* across the membrane is zero. At this potential, the electrical gradient perfectly opposes the chemical (concentration) gradient.

### Formula

The Nernst equation calculates this potential for an individual ion:

`E = - (2.3 * R * T / z * F) * log₁₀ [ [C]_in / [C]_out ]`

### Components of the Nernst Equation

*   **R (Ideal Gas Constant):** `R = 8.314 J·K⁻¹·mol⁻¹`. The value in the notes is `8.135 J·K⁻¹·mol⁻¹`.
*   **T (Absolute Temperature):** Measured in Kelvin (K).
*   **z (Valency):** The electrical charge of the ion.
    *   For Na⁺, z = +1
    *   For K⁺, z = +1
    *   For Ca²⁺, z = +2
    *   For Cl⁻, z = -1
*   **F (Faraday's Constant):** The electric charge per mole of electrons. `F ≈ 9.6485 x 10⁴ C·mol⁻¹`. The value in the notes is `9.684 x 10⁴ C·mol⁻¹`.
*   **[C]_in / [C]_out:** The ratio of the ion's concentration inside to outside the cell.

### Simplified Example

At typical body temperature, the term `(2.3 * R * T / F)` can be simplified to approximately `60 mV`. For an ion like Sodium (Na⁺) with a valency `z = +1`, the equation simplifies. If we consider the standard Nernst form `E = (60mV/z) * log₁₀([C]_out/[C]_in)`, and a typical `[Na⁺]_out/[Na⁺]_in` ratio of 10, the result is:

`E_Na⁺ = (60 mV / +1) * log₁₀(10) = +60 mV`

---
# Different Types of Ion Channels

Ion channels are pore-forming membrane proteins that allow ions to pass through the channel pore. Their functions include establishing a resting membrane potential, shaping action potentials and other electrical signals, and regulating cell volume. They are crucial components in the nervous system and muscle tissues. Ion channels can be specific to certain ions, such as cations (e.g., Na+, K+, Ca2+) or anions (e.g., Cl-).

## 1. ATP-Powered Pumps: The Sodium-Potassium Pump

The Sodium-Potassium pump (Na+/K+-ATPase) is not a channel, but a critical active transport pump that establishes and maintains the concentration gradients for sodium and potassium ions across the cell membrane.

*   **Mechanism:** It actively pumps **3 Sodium ions (Na+) out** of the cell and **2 Potassium ions (K+) into** the cell for each molecule of ATP hydrolyzed.
*   **Electrogenic Nature:** Since it pumps more positive charge out than in, it creates a net negative charge inside the cell. This direct contribution to the membrane potential is small, generating about **-5mV**.
*   **Resting Potential:** Its primary role is creating the steep concentration gradients that other channels (like leaky channels) use to generate the majority of the resting membrane potential. The resting potential in a typical neuron is between **-80mV and -90mV**.

## 2. Leaky Potassium (K+) Channels

Leaky channels are passive channels that are typically always open, allowing ions to move down their electrochemical gradient.

*   **Function:** Leaky K+ channels allow potassium ions, which are highly concentrated inside the cell (due to the Na+/K+ pump), to diffuse out. 
*   **Basis of Operation:** This movement is driven by the **concentration gradient** (more K+ inside) and opposed by the **electronegativity** of the cell's interior (the negative charge inside attracts the positive K+ ions).
*   **Equilibrium Potential:** An ion's movement will stop when the electrical force pulling it in perfectly balances the concentration gradient pushing it out. This point of balance is called the **Equilibrium Potential (E.P.)**. The high permeability of the resting membrane to K+ is the main reason the resting potential is close to the equilibrium potential for potassium.

## 3. Sodium (Na+) Channels

These channels control the movement of sodium ions across the membrane.

*   **Function:** They facilitate the controlled flow of Na+ ions, typically into the cell, driven by a strong electrochemical gradient. The influx of Na+ causes the membrane potential to become less negative (depolarization).
*   **Permeability:** The permeability of these channels is tightly regulated, often by voltage or ligands.

## 4. Chlorine (Cl-) Channels

These channels are specific to the anion chloride (Cl-). The influx of this negatively charged ion typically causes hyperpolarization (making the cell more negative) or helps to stabilize the resting membrane potential.

## 5. Voltage-Gated Channels

Voltage-gated channels are a class of transmembrane proteins that are activated by changes in the electrical membrane potential near the channel.

*   **Mechanism:** They have a sensor that detects changes in voltage, causing the channel to open or close.
*   **Importance:** They are essential for generating and propagating action potentials in excitable cells like neurons and muscle cells.
*   **Examples:** Common examples include the **voltage-gated Na+ channel** (responsible for the rapid depolarization phase of an action potential) and the **voltage-gated K+ channel** (responsible for repolarization).

## 6. Ligand-Gated Channels

Ligand-gated channels open to allow ions to pass through the membrane in response to the binding of a chemical messenger (a ligand), such as a neurotransmitter.

![Diagram of a Ligand-Gated Channel](images/3/image_1.png)

*   **Mechanism:** As described in the notes, a stimulus molecule (e.g., calcium, Ca2+) binds to a specific **receptor** site on the channel protein. This binding event causes a conformational change in the protein, opening the channel pore.
*   **Example Context (Neuromuscular Junction):** A classic example is at the neuromuscular junction. A neuron releases a neurotransmitter (the ligand) which binds to receptors on a muscle cell. This opens ligand-gated ion channels, allowing ions like calcium to flow into the muscle cell, triggering contraction.

---
# Signal Propagation Mechanism in Excitable Cells

This document explains the mechanism of signal propagation in excitable cells, such as neurons, focusing on a pressure-sensitive neuron. The core of this mechanism is the **action potential**, a rapid, temporary change in the cell's membrane potential.

## 1. The Resting State and Ion Channels

An excitable cell at rest maintains a **Resting Membrane Potential (RMP)**, which is typically around -70mV. This negative charge inside the cell relative to the outside is established and maintained by several key components embedded in the cell membrane.

![Diagram of ion channels and pumps in an excitable cell membrane](images/4/image_1.png)

*   **Na+/K+ ATPase Pump:** This active transport protein pumps three Sodium ions (Na+) out of the cell for every two Potassium ions (K+) it pumps in. This action consumes ATP and is crucial for maintaining the steep concentration gradients for both ions across the membrane.
*   **Leaky K+ Channels:** These channels are always open, allowing K+ ions to diffuse out of the cell down their concentration gradient (from high concentration inside, ~140 mmole/lt, to low concentration outside, ~4 mmole/lt). This outflow of positive charge is the primary contributor to the negative RMP.
*   **Voltage-Gated Channels:** These channels are closed at rest but open in response to changes in the membrane potential. There are specific voltage-gated channels for Na+ and K+, which are essential for generating the action potential.
*   **Stimulus-Gated Channels:** In this specific example of a pressure-sensitive neuron, there are mechanically-gated channels that open in response to physical pressure.

## 2. The Action Potential Cycle

The action potential is a stereotyped sequence of events that occurs when a stimulus depolarizes the membrane to a specific **threshold** value (around -60mV). It follows an 'all-or-none' principle: if the threshold is reached, a full action potential is fired; if not, nothing happens.

![Graph of voltage vs. time during an action potential](images/4/image_2.png)

The cycle can be broken down into the following phases:

1.  **Stimulus and Initial Depolarization:** A mechanical stimulus (pressure) opens pressure-sensitive channels, allowing Na+ to flow into the cell. This influx of positive ions makes the membrane potential less negative, causing it to rise from the RMP of -70mV.

2.  **Threshold and Rapid Depolarization:** If the initial stimulus is strong enough to depolarize the membrane to the threshold potential (~-60mV), voltage-gated Na+ channels are triggered to open. This results in a massive, rapid influx of Na+, causing the membrane potential to shoot up towards a peak of about +10mV. This phase is the **depolarization** or the rising phase of the action potential.

3.  **Repolarization:** At the peak of the action potential, the voltage-gated Na+ channels inactivate, stopping the influx of Na+. Simultaneously, the slower voltage-gated K+ channels open. K+ ions rush out of the cell, down their electrochemical gradient, causing the membrane potential to rapidly fall back towards the resting level. This is the **repolarization** or falling phase.

4.  **Hyperpolarization (Undershoot):** The voltage-gated K+ channels are slow to close. As a result, they remain open slightly longer than necessary, allowing excess K+ to leave the cell. This causes the membrane potential to briefly become more negative than the RMP, a phase known as **hyperpolarization**.

5.  **Return to Resting State:** The voltage-gated K+ channels finally close. The Na+/K+ ATPase pump continues to work to restore the original ion concentration gradients, bringing the membrane potential back to its resting level of -70mV.

## 3. Refractory Periods

Following an action potential, the neuron enters a state where it is less responsive to new stimuli.

*   **Absolute Refractory Period:** During depolarization and most of repolarization, the voltage-gated Na+ channels are either already open or in an inactivated state. In this period, it is impossible to generate a second action potential, regardless of the stimulus strength.

*   **Relative Refractory Period:** During hyperpolarization, the membrane is more negative than at rest. While the Na+ channels have reset, a stronger-than-usual stimulus is required to depolarize the membrane all the way to the threshold to fire another action potential.

---

# Neurophysiology: Ion Channels and Signal Transmission

This document covers the fundamental principles of neuronal signal transmission, focusing on the behavior of voltage-sensitive sodium channels and comparing two methods of signal propagation along an axon.

## 1. Voltage-Sensitive Na+ Channel

Voltage-sensitive (or voltage-gated) sodium (Na+) channels are integral membrane proteins that are crucial for initiating and propagating action potentials in neurons and other excitable cells. Their function is to allow Na+ ions to rapidly flow into the cell, causing depolarization. These channels can exist in three main conformational states.

![Diagram showing the three states of a voltage-gated sodium channel](images/5/image_1.png)

### States of the Na+ Channel

1.  **Resting State (Closed but capable of opening):** In this state, the channel is closed, but it is ready to open in response to a sufficient voltage change (depolarization). This is the state of the channel at the neuron's resting membrane potential.
2.  **Active State (Open):** Upon reaching a threshold voltage, the channel rapidly changes conformation and opens. This allows a massive influx of Na+ ions into the cell, down their electrochemical gradient, leading to the rapid upstroke of the action potential.
3.  **Inactive State (Closed and not capable of opening):** Shortly after opening, the channel spontaneously closes again, but into an inactivated state. In this state, an 'inactivation gate' blocks the pore. The channel cannot be opened by further depolarization until the membrane potential returns to its resting state, which allows the inactivation gate to reopen and the channel to return to the resting state. This mechanism is responsible for the **absolute refractory period**.

### Timeline of Channel States During an Action Potential

*   `t0 - t1`: **Resting State**. The neuron is at its resting potential, and the Na+ channels are closed.
*   `t1 - t2`: **Active State**. A stimulus causes the membrane to depolarize to threshold, causing Na+ channels to open. Na+ rushes in, causing the rapid depolarization phase of the action potential.
*   `t2 - t3`: **Inactive State**. The Na+ channels inactivate. During this time, voltage-gated Potassium (K+) channels are typically open (`t2 - t4`), allowing K+ to exit the cell, which causes the repolarization of the membrane.
*   `t3 - t4`: **Return to Resting State**. As the membrane repolarizes and returns to its resting potential, the Na+ channels transition from the inactive state back to the closed, resting state, ready for the next action potential.

## 2. Signal Transmission Methods

Signal transmission, or action potential propagation, occurs via two primary methods depending on whether the axon is myelinated or not.

### Method I: Continuous Conduction (Unmyelinated Axons)

This method occurs in axons that lack a myelin sheath. The action potential propagates as a continuous wave along the entire length of the axon.

![Diagram illustrating continuous conduction in an unmyelinated axon](images/5/image_2.png)

**Process:**
1.  An initial stimulus causes a localized depolarization, opening voltage-gated Na+ channels.
2.  The influx of Na+ at this point creates a 'local voltage' change that depolarizes the adjacent segment of the membrane to its threshold.
3.  This triggers the opening of Na+ channels in that adjacent segment, regenerating the action potential. Meanwhile, the previous segment begins to repolarize as K+ channels open and Na+ channels inactivate.
4.  This chain reaction continues step-by-step along the entire axon membrane.

**Key Characteristic:**
*   **Slower Speed:** As the note indicates, this method is relatively slow because the action potential must be regenerated at every single point along the membrane. The Na+/K+ ATPase pump works continuously to restore the ion gradients after the action potential has passed.

### Method II: Saltatory Conduction (Myelinated Axons)

This is a much faster method of signal propagation that occurs in myelinated axons.

![Diagram illustrating saltatory conduction in a myelinated axon](images/5/image_3.png)

**Process:**
1.  The axon is wrapped in a **myelin sheath**, an insulating layer that is a poor electrical conductor.
2.  This sheath is interrupted at regular intervals by gaps called **Nodes of Ranvier**, where the voltage-gated Na+ and K+ channels are concentrated.
3.  An action potential is generated at one node (e.g., triggered by a pressure-sensitive Na+ channel in a sensory neuron).
4.  The influx of Na+ ions does not trigger adjacent channels immediately. Instead, the ions diffuse rapidly through the cytoplasm under the insulating myelin sheath to the next Node of Ranvier.
5.  This diffusion of charge depolarizes the next node to its threshold, triggering a new action potential.

**Key Characteristic:**
*   **Faster Speed:** The action potential appears to 'jump' from node to node, hence the name 'saltatory' (from the Latin *saltare*, to leap). This is much faster and more energy-efficient than continuous conduction.

## 3. Refractory Period

The **refractory period** is a brief period of time following an action potential during which it is more difficult or impossible for the neuron to generate another action potential.

*   **Absolute Refractory Period:** This corresponds to the time when the voltage-gated Na+ channels are in their **inactive state**. No matter how strong the stimulus, a new action potential cannot be generated. This ensures the one-way propagation of the nerve impulse and limits the maximum firing rate of the neuron.

---

# Neuronal Signaling: Action Potentials and Synaptic Transmission

This document outlines the fundamental processes of neural communication, covering the generation of an action potential within a single neuron and the transmission of that signal to another neuron across a synapse.

## 1. The Action Potential (AP)

An **Action Potential** is a rapid, temporary change in the electrical potential across the membrane of an excitable cell, such as a neuron. It functions as a moving wave of electrical activity, formally described as a wave of **depolarization** followed by **repolarization** that propagates along the cell membrane.

### Structure of a Neuron

Neurons are the primary cells of the nervous system. An action potential is initiated at one end and travels down the length of the neuron to transmit a signal.

![Diagram of a myelinated neuron showing its key components.](images/6/image_1.png)

Key components of a neuron include:

*   **Soma (Cell Body):** Contains the **nucleus** and is the main metabolic center of the neuron.
*   **Dendrites:** Tree-like extensions that receive signals from other neurons.
*   **Axon:** A long, slender projection that conducts electrical impulses away from the soma.
*   **Myelin Sheath:** A fatty insulating layer that covers the axon, formed by **Schwann Cells**. It significantly increases the speed of signal transmission.
*   **Nodes of Ranvier:** Gaps in the myelin sheath where the action potential is regenerated.
*   **Axon Terminal:** The end of the axon, where the signal is passed to the next cell.

### Generation and Propagation of an Action Potential

The process begins when a stimulus (e.g., pressure on a sensitive cell) causes specific ion channels in the neuron's membrane to open. This allows an influx of positive ions (like `Na+`), raising the membrane potential. If this potential reaches a certain **threshold**, a full-scale action potential is triggered, which then travels down the axon.

### Conduction Speed

The speed at which an action potential travels depends on whether the axon is myelinated.

*   **Myelinated Neuron:** The signal jumps from one Node of Ranvier to the next (a process called saltatory conduction), resulting in very fast transmission speeds of approximately **100 m/sec**.
*   **Non-myelinated Neuron:** The signal must propagate continuously along the entire axon membrane, which is much slower, around **0.25 m/sec**.

## 2. Transmission of the Signal (Synaptic Transmission)

For a signal to travel through the nervous system, it must be passed from one neuron to the next, or from a neuron to a target cell like a muscle fiber (at a **neuromuscular joint**). This transfer occurs at a specialized junction called a **synapse**.

### The Chemical Synapse

The process of transmitting an action potential across a chemical synapse involves converting the electrical signal into a chemical one and then back into an electrical signal.

![Diagram illustrating the process of synaptic transmission between two neurons.](images/6/image_2.png)

The key steps are as follows:

1.  **Arrival of AP:** The action potential arrives at the axon terminal of the **presynaptic (1st) neuron**.
2.  **Calcium Influx:** The change in voltage opens **voltage-gated calcium channels**, allowing `Ca²⁺` ions to flow into the terminal.
3.  **Neurotransmitter Release:** The influx of `Ca²⁺` triggers proteins like **Syntaxin** (a calcium-sensitive protein) to cause vesicles filled with neurotransmitters (e.g., **Acetylcholine**) to fuse with the presynaptic membrane. The neurotransmitters are then released into the **synaptic cleft** (the space between the neurons).
4.  **Receptor Binding:** Neurotransmitters diffuse across the cleft and bind to **ligand-gated ion channels** on the membrane of the **postsynaptic (2nd) neuron**.
5.  **Postsynaptic Potential:** This binding opens the channels, allowing ions like `Na⁺` to flow into the postsynaptic neuron. This influx of positive charge creates a new electrical potential. If this potential is strong enough to reach the threshold, it will trigger a new action potential in the second neuron.

This entire process effectively converts the electrical **Action Potential** into a **Chemical Signal** (neurotransmitter) to cross the synapse, and then back into an electrical signal.

### The Action Potential Waveform

The change in membrane potential during an action potential follows a characteristic pattern when plotted against time.

![Graph of membrane potential versus time during an action potential.](images/6/image_3.png)

The phases shown in the graph are:

*   **Resting Membrane Potential (RMP):** The baseline, negative charge of the neuron at rest.
*   **Threshold:** The minimum potential that must be reached to trigger an action potential.
*   **Depolarization (Rising Phase):** A rapid increase in potential due to the influx of `Na⁺` ions.
*   **Repolarization (Falling Phase):** A rapid decrease in potential as `K⁺` ions exit the cell.
*   **Hyperpolarization:** A brief period where the potential drops below the RMP.

The entire event is very brief, typically lasting only a few milliseconds (e.g., ~5 ms).

---

# Mechanism of Signal Transmission in Excitable Cells

Excitable cells, such as neurons and muscle cells, have the ability to generate and propagate electrical signals called action potentials. The transmission of these signals between cells is fundamental for processes like thought, movement, and heartbeat. This document outlines the three primary mechanisms of signal transmission between these cells.

## 1. Transmission Between Two Neurons (Chemical Synapse)

This is the most common type of synapse in the nervous system. It involves the conversion of an electrical signal (action potential) in the first neuron into a chemical signal (neurotransmitter release), which then generates an electrical signal in the second neuron. This junction is also referred to as a nerve cell joint.

![Diagram of a chemical synapse between two neurons](images/7/image_1.png)

### Sequence of Events:
1.  **Arrival of Action Potential:** An action potential travels down the axon of the presynaptic (first) neuron and reaches the nerve ending, also known as the axon terminal.
2.  **Calcium Influx:** The depolarization from the action potential opens voltage-gated calcium (Ca²⁺) channels. Ca²⁺ ions flow from the extracellular space into the presynaptic terminal.
3.  **Vesicle Fusion and Neurotransmitter Release:** The influx of Ca²⁺ triggers the fusion of synaptic vesicles with the presynaptic membrane. This process is mediated by SNARE proteins, such as **Syntaxin** on the presynaptic membrane and **Synaptobrevin** on the vesicle membrane. These vesicles contain chemical messengers called neurotransmitters (in this case, **Acetylcholine**).
4.  **Diffusion Across Synaptic Cleft:** The neurotransmitter is released into the synaptic cleft, a small gap (~70 nm) between the two neurons, and diffuses across it.
5.  **Binding to Postsynaptic Receptors:** The neurotransmitter binds to specific receptor proteins on the postsynaptic membrane of the second neuron (the dendrite). The example shows a **Nicotinic Acetylcholine Receptor**, which is a type of ligand-gated ion channel and is a pentameric protein (composed of five subunits).
6.  **Postsynaptic Potential Generation:** Binding of acetylcholine opens the ion channel, allowing sodium ions (Na⁺) to flow into the postsynaptic neuron. This influx of positive charge causes a localized depolarization called an excitatory postsynaptic potential (EPSP). If this potential is strong enough to reach the threshold, it will trigger a new action potential in the second neuron.

## 2. Transmission Between a Motor Neuron and Skeletal Muscle (Neuromuscular Junction)

This is a specialized chemical synapse where a motor neuron communicates with a skeletal muscle fiber, causing it to contract. This process is known as Excitation-Contraction (E-C) coupling. The postsynaptic membrane on the muscle cell is called the **motor end plate**.

![Diagram of Excitation-Contraction Coupling in a muscle cell](images/7/image_2.png)

### Sequence of Events:
1.  **Action Potential Propagation:** An action potential generated at the motor end plate travels along the muscle cell's membrane (sarcolemma) and down into invaginations called **T-tubules**.
2.  **Voltage Sensing:** The depolarization is detected by the **Dihydropyridine Receptor (DHPR)**, a voltage-sensitive protein located in the T-tubule membrane.
3.  **Calcium Release:** In skeletal muscle, the DHPR is mechanically coupled to the **Ryanodine Receptor (RyR)**, which is a Ca²⁺ release channel located on the membrane of the **Sarcoplasmic Reticulum** (SR), a specialized organelle that stores high concentrations of calcium.
4.  **Initiation of Contraction:** The activation of the DHPR physically pulls open the RyR channel, allowing a massive amount of Ca²⁺ to flood from the SR into the cytoplasm. This increase in cytoplasmic Ca²⁺ initiates the process of muscle contraction.

## 3. Transmission Between Two Muscle Cells (Electrical Synapse)

This type of transmission is characteristic of cardiac muscle and some types of smooth muscle. It allows for rapid and synchronized contraction of an entire muscle tissue mass. It relies on direct electrical coupling between cells rather than chemical messengers.

![Diagram of a gap junction between two muscle cells](images/7/image_3.png)

### Mechanism:
*   **Gap Junctions:** Adjacent muscle cells (**myocytes**) are physically connected by protein channels called **gap junctions**. These junctions form pores that allow the cytoplasm of the two cells to be continuous.
*   **Direct Ion Flow:** When an action potential occurs in one cell, ions (like Na⁺) that rush into the cell can flow directly into the adjacent cell through the gap junctions.
*   **Signal Propagation:** This direct flow of current depolarizes the neighboring cell to its threshold, causing it to fire an action potential as well. This process repeats, allowing the wave of excitation to spread rapidly and uniformly throughout the tissue, ensuring a coordinated contraction.

---

