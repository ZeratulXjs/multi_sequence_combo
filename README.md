This is a small program to combine sequences in .FASTA format before performing a multiple sequence alignment.
I wrote it in Linux; this assumes you have Python already installed (version does not matter, it's a really simple program)

Only the `fasta_combine.py` is necessary. 
However, if you want to see how it works out of the box, here's how.....

# To test it, run the following from your terminal;

1. Clone this repo to your machine (preferably the Desktop but that's up to you)

``` git clone https://github.com/ZeratulXjs/multi_sequence_combo ```


2. CD into the directory

``` cd multi_sequence_combo ```

3. Generate a list of the sample .FASTA files 
``` ls single_sequences > sequence_folder_contents.txt ```

4. Run the python file, which will use the generated list to combine the files into one .FASTA file
``` python fasta_combine.py ```

5. It will generate a file called `combined_sequences.fasta` that contains all the sequences


# To run this on your own sequences;
1. Replace the sample files with your own sequences (in .FASTA) retrieved from NCBI or any other sequence database.
2. Start from step 2 of the test.
