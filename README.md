# CAR-PUF Defintion and Working
The Companion Arbiter PUF (CAR-PUF) is an advanced Physical Unclonable Function (PUF) designed to enhance the security of hardware systems by exploiting the inherent variation in the manufacturing process of Integrated Circuits (ICs). These differences are difficult to clone or predict.

### 1. **Basic Structure**
   - **Arbiter PUF**: The Arbiter PUF consists of multiple delay paths. These paths are arranged in pairs, with a final arbiter that decides which signal arrives first. Due to manufacturing variability, each PUF has unique delay characteristics. Even with the same challenge, different instances of the same PUF will produce different responses.
   - **Companion PUF**: CAR-PUF adds a "companion" structure, which is typically a simple XOR function or another delay-based PUF. The companion is designed to interact with the original Arbiter PUF in a way that makes the system more resistant to modeling attacks. The companion structure increases the unpredictability of the output. By adding a secondary processing layer, the CAR-PUF makes it significantly harder for attackers to model the behavior of the PUF, thus enhancing security.


### 2. **Challenge-Response Mechanism**
   - **Challenge**: A binary input stream is fed into the PUF, which determines the configuration of the delay paths. The length of the challenge determines the complexity of the system.
   - **Response**: The arbiter measures the difference in delay between the two paths and produces a binary output. In the CAR-PUF, the response is further processed by the companion structure, making the response more complex and less predictable.


### 4. **Applications**
   - **Authentication**: CAR-PUFs are used in secure authentication protocols where the challenge-response pairs serve as cryptographic keys.
   - **Key Generation**: They can be used to generate cryptographic keys that are unique to each device, ensuring that the keys cannot be cloned or reproduced.
   - **Hardware Security**: CAR-PUFs are valuable in protecting against counterfeiting and unauthorized access to hardware devices.

### 5. **Advantages**
   - **Increased Robustness**: The companion structure adds an extra layer of security, making the system more resistant to attacks.
   - **Scalability**: CAR-PUFs can be implemented in various types of ICs, making them suitable for a wide range of applications.
   - **Low Power Consumption**: Despite the additional complexity, CAR-PUFs are designed to operate efficiently, making them suitable for low-power devices.

### 6. **Challenges**
   - **Design Complexity**: The addition of the companion structure increases the design complexity, which might lead to more challenges in manufacturing.
   - **Environmental Sensitivity**: Like other PUFs, CAR-PUFs can be sensitive to environmental changes, such as temperature and voltage variations, which can affect the reliability of the responses.

In summary, the CAR-PUF enhances the security of traditional Arbiter PUFs by introducing a companion mechanism that adds complexity and unpredictability, making it a powerful tool in hardware security applications.

# Objective
The objective is to crack the CAR-PUF (Physically Unclonable Function) using CSVMs, given challenge-response pairs as a dataset. 

# Datasets

# Methodology

# Conclusions

