# Falcon_recovery_OLSattack
This code implements a secret key recovery attack, called OLS attack, on Falcon. The OLS attack is a simple linear estimator that effectively recovers secret keys in GPV signatures by leveraging partial information about the signature. We also presents the efficient OLS attack which efficiently reduces the number of side channel attacks by using property of NTRU lattice. For a detailed explanation and theoretical background of the OLS attack and the efficient OLS attack, please refer to the paper https://eprint.iacr.org/2024/2043. The reference files used in this implementation are based on the Falcon python reference code originally developed by Thomas Prest, ensuring compatibility and reliability https://github.com/tprest/falcon.py. We have modified the original refernce code (falcon.py and ffsampling.py) to extract partial information from the signature, enabling the execution of the OLS attack.

# Setup
This code does not require a complex directory structure. The only essential requirement is the ability to run the Falcon python reference code  https://github.com/tprest/falcon.py. Before running this implementation, we recommend testing the Falcon reference code to ensure it functions correctly. If the reference test files run successfully, this code should also work without issues.

# How to use?
Using this implementation is straightforward:
1. Open `OLS_attack.py` or `Eff_OLS_attack.py` and adjust the `N` to set the desired dimension for the secret polynomial. 
2. Modify `sam_num` to specify the number of samples used in the OLS attack.
3. Run `OLS_attack.py` or `Eff_OLS_attack.py` in the terminal to execute sample collection and the OLS attack process.

This should allow you to perform the attack efficiently with minimal configuration. If you wish to modify the OLS attack or the efficient OLS attack, you can do so by editing `falcon.py`. Specifically, you can alter the `OLS_attack` or `Eff_OLS_attack` to implement a different linear estimator or introduce a new type of estimator, such as a ridge estimator, elastic net estimator, or lasso estimator. Additionally, if you want to modify the method for extracting partial information, you should modify the `sample_preimage` function and its internal function `ffsampling_fft2`. The `ffsampling_fft2` function is a modified version of `ffsampling_fft`, specifically designed to extract partial information.


# Performance of these OLS attacks
<p align="center">
  <img src="https://github.com/user-attachments/assets/27785d52-599b-44a2-af73-f2727c86f5c7" alt="image">
</p>

The equation ![Equation](https://quicklatex.com/cache3/96/ql_026eb67ea7a6ebff0263f9fb93f24b96_l3.png) and ![equation](https://quicklatex.com/cache3/d5/ql_7a71a2f27adfdd7a64c25a05a8e4edd5_l3.png) represent the estimator in `OLS attack.py` and `Eff_OLS_attack.py`, respectively. This table illustrates that the average number of samples and time required for achieving particular success rate (SR) to recover the secret key of Falcon-256, 512, and 1024 by the OLS attack. For further details, please refer to the paper https://eprint.iacr.org/2024/2043.

# Research team and contact information
Supervising professor
- Dong June Shin (Haynang University) / djshin@hanynag.ac.kr
  
Researchers
- Jaesang Noh / darkelzm@hanyang.ac.kr
- Hyunseo Choi / hyun123456a@hanyang.ac.kr
- Dongwoo Han / hdw0131@hanyang.ac.kr
- Seunghwan Lee / kr3951@hanyang.ac.kr
- Hyeonggeon Joo / hgjoo2021@gmail.com
- Dohyeok Kim / dohyuk1000@hanyang.ac.kr
- Youngjun Kim / june0888@hanyang.ac.kr
- Taejeong Kim / birdy0212@hayang.ac.kr
- Shin Kim / thegimsin@hanyang.ac.kr
    
Research lab website: http://ccrl.hanyang.ac.kr 

This research team is affiliated with Hanyang University and is engaged in advanced research in cryptography. For further inquiries, please refer to the contact details provided above.

