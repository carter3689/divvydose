from tabula import read_pdf, convert_into

df = read_pdf("Document44.pdf", encoding = "ISO-8859-1", output_format="csv")

print(df)

data = convert_into("Document44.pdf", "blackboard_jungle.csv", output_format='csv', encoding = "ISO-8859-1")