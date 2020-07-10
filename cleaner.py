import xlsxwriter


def clean_sequences(sequenceFile):
    accession_ids = []
    sequences = []
    char_counter = 0
    sequence = ''

    # Will 'clean' accession ids and also create a list of all the sequences
    with open(sequenceFile, "r") as file:
        for line in file:
            flag = 0

            if line[0] == ">":
                char_counter += 1

            if line[0] == ">" and "." in line:
                line = line[1:]
                line = line[:-3]
                accession_ids.append(line)
                flag = 1

            if line[0] == ">" and "." not in line:
                line = line[1:]
                line = line[:-1]
                accession_ids.append(line)
                flag = 1

            if flag == 0:
                sequence += line.rstrip()

            if (char_counter - len(sequences)) == 2:
                sequences.append(sequence)
                sequence = ''
                
        # This code snippet will get the last sequence that the for loop couldn't.
        sequences.append(sequence)

        # Will create xslx file with sequences and accession_ids
        new_file = xlsxwriter.Workbook("formatted_sequences.xlsx")
        outSheet = new_file.add_worksheet()

        num = 1
        for count in range(len(sequences)):
            outSheet.write(f"A{num}", accession_ids[count])
            outSheet.write(f"B{num}", sequences[count])
            num += 1

        new_file.close()
        print(f"Total number of sequences is: {len(sequences)}")


clean_sequences("YOUR_SEQUENCE_FILE:"
                # format should be:
                    # > Accession_num_1
                    # MFVFLVLLPL............
                    # > Accession_num_2
                    # MFVFLVLLPL............
                "")

