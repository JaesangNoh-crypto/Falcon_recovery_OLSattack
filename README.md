# Falcon_recovery_OLSattack
This code implements a secret key recovery attack, called OLS attack, on Falcon. The OLS attack is a simple linear estimator that effectively recovers secret keys in GPV signatures by leveraging partial information about the signature. For a detailed explanation and theoretical background of the OLS attack, please refer to the paper https://eprint.iacr.org/2024/2043. The reference files used in this implementation are based on the Falcon python reference code originally developed by Thomas Prest, ensuring compatibility and reliability https://github.com/tprest/falcon.py. We have modified falcon.py and ffsampling.py to extract partial information from the signature, enabling the execution of the OLS attack.

# Setup
This code does not require a complex directory structure. The only essential requirement is the ability to run the Falcon reference code. Before running this implementation, we recommend testing the Falcon reference code to ensure it functions correctly. If the reference test files run successfully, this code should also work without issues.

# How to use?
Using this implementation is straightforward:
1. Open "OLS_attack.py" and adjust the "N" to set the desired dimension for the secret polynomial. 
2. Modify "sam_num" to specify the number of samples used in the OLS attack.
3. Run "OLS_attack.py" in the terminal to execute sample collection and the OLS attack process.

This should allow you to perform the attack efficiently with minimal configuration.

