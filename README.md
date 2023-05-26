# CrackUser

CrackUser is a powerful Python tool designed to assist in generating customized wordlists for password cracking. By utilizing information provided by the user, CrackUser creates a comprehensive list of possible password combinations, with a particular focus on strings that the target person may potentially use in their passwords. It incorporates the option to input a hashcat hashtable to create even more combinations of the passwords.

## Key Features

- **Customized Wordlist Generation**: CrackUser allows users to input specific information about the target person, such as their name, birthdate, hobbies, interests, and any other relevant details. It intelligently analyzes this information to generate a wordlist containing possible password combinations.

- **Targeted String Identification**: The tool employs advanced algorithms to identify and include strings that are commonly associated with the target person. By incorporating these strings into the wordlist, CrackUser increases the chances of finding a successful password match.

- **Hashcat Hashtable Integration**: CrackUser integrates seamlessly with hashcat, a popular password recovery tool. Users can input a hashcat hashtable into CrackUser, which expands the generated wordlist by leveraging the precomputed hash values, significantly increasing the number of potential password combinations.

- **Password Complexity Options**: CrackUser provides options to adjust the complexity of generated passwords based on the user's requirements. Users can specify the minimum and maximum length, character types (uppercase, lowercase, digits, special characters), and other parameters to tailor the wordlist to their needs.

- **Export and Save**: Once the wordlist generation process is complete, CrackUser allows users to export and save the generated wordlist in various file formats, such as TXT or CSV, for further analysis or use with password cracking tools.

## Getting Started

To get started with CrackUser, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/CrackUser.git
