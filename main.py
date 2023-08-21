from tkinter import *


root = Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.iconbitmap("bill_120383.ico")

headingLabel = Label(
    root,
    text="Retail Billing System",
    font=("times new roman", 30, "bold"),
    bg="gray20",
    fg="gold",
    bd=12,
    relief=GROOVE,  # for border styling
)
headingLabel.pack(fill=X)  # fill the entire width label

# custor details frame
customDeFrame = LabelFrame(
    root,
    text="Customer Details",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)  # only you can see this after adding contents
customDeFrame.pack(fill=X, pady=10)

nameLabel = Label(
    customDeFrame,
    text="Name",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customDeFrame, font=("arial", 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(
    customDeFrame,
    text="Phone Number",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
phoneLabel.grid(row=0, column=2, padx=20)

phoneEntry = Entry(customDeFrame, font=("arial", 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billNumLabel = Label(
    customDeFrame,
    text="Bill Number",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
billNumLabel.grid(row=0, column=4, padx=20)

billNumEntry = Entry(customDeFrame, font=("arial", 15), bd=7, width=18)
billNumEntry.grid(row=0, column=5, padx=8)

searchButton = Button(
    customDeFrame, text="SEARCH", font=("arial", 12, "bold"), bd=7, width=10
)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productFrame = Frame(root)
# diff btw frame and label frame class is frame does not have a label but label frame have label

productFrame.pack(fill=X, pady=5)  # pack simply pack everything one after another

cosmeticsFrame = LabelFrame(
    productFrame,
    text="Cosmetics",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)
cosmeticsFrame.grid(row=0, column=0)

bathSoupLabel = Label(
    cosmeticsFrame,
    text="Bath Soup",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
bathSoupLabel.grid(sticky="w", row=0, column=0, padx=8, pady=8)

bathSoupEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
bathSoupEntry.grid(row=0, column=1, padx=8, pady=8, sticky="w")

faceCreamLabel = Label(
    cosmeticsFrame,
    text="Face Cream",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
faceCreamLabel.grid(row=1, column=0, padx=8, pady=8)

faceCreamEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
faceCreamEntry.grid(sticky="w", row=1, column=1, padx=8, pady=8)

faceWashLabel = Label(
    cosmeticsFrame,
    text="Face Wash",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
faceWashLabel.grid(sticky="w", row=2, column=0, padx=8, pady=8)

faceWashEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
faceWashEntry.grid(row=2, column=1, padx=8, pady=8, sticky="w")

hairSprayLabel = Label(
    cosmeticsFrame,
    text="Hair Spray",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
hairSprayLabel.grid(sticky="w", row=3, column=0, padx=8, pady=8)

hairSprayEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
hairSprayEntry.grid(row=3, column=1, padx=8, pady=8)

hairGelLabel = Label(
    cosmeticsFrame,
    text="Hair Gel",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
hairGelLabel.grid(sticky="w", row=4, column=0, padx=8, pady=8)

hairGelEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
hairGelEntry.grid(row=4, column=1, padx=8, pady=8)

bodyLotionLabel = Label(
    cosmeticsFrame,
    text="Body Lotion",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
bodyLotionLabel.grid(sticky="w", row=5, column=0, padx=8, pady=8)

bodyLotionEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
bodyLotionEntry.grid(row=5, column=1, padx=8, pady=8)


groceryFrame = LabelFrame(
    productFrame,
    text="Grocery",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)
groceryFrame.grid(row=0, column=1)

riceLabel = Label(
    groceryFrame,
    text="Rice",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
riceLabel.grid(sticky="w", row=0, column=0, padx=8, pady=8)

riceEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
riceEntry.grid(row=0, column=1, padx=8, pady=8, sticky="w")

oilLabel = Label(
    groceryFrame,
    text="Oil",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
oilLabel.grid(sticky="w", row=1, column=0, padx=8, pady=8)

oilCreamEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
oilCreamEntry.grid(row=1, column=1, padx=8, pady=8)

daalLabel = Label(
    groceryFrame,
    text="Daal",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
daalLabel.grid(sticky="w", row=2, column=0, padx=8, pady=8)

daalEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
daalEntry.grid(row=2, column=1, padx=8, pady=8, sticky="w")

wheatLabel = Label(
    groceryFrame,
    text="Wheat",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
wheatLabel.grid(sticky="w", row=3, column=0, padx=8, pady=8)

wheatEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
wheatEntry.grid(row=3, column=1, padx=8, pady=8)

sugarLabel = Label(
    groceryFrame,
    text="Sugar",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
sugarLabel.grid(sticky="w", row=4, column=0, padx=8, pady=8)

sugarEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
sugarEntry.grid(row=4, column=1, padx=8, pady=8)

teaLabel = Label(
    groceryFrame,
    text="Tea",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
teaLabel.grid(sticky="w", row=5, column=0, padx=8, pady=8)

teaEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
teaEntry.grid(row=5, column=1, padx=8, pady=8)


coolDrinkFrame = LabelFrame(
    productFrame,
    text="Cool Drinks",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)

coolDrinkFrame.grid(row=0, column=2)

maazaLabel = Label(
    coolDrinkFrame,
    text="Maaza",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
maazaLabel.grid(sticky="w", row=0, column=0, padx=8, pady=8)

maazaEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
maazaEntry.grid(row=0, column=1, padx=8, pady=8, sticky="w")

pepsiLabel = Label(
    coolDrinkFrame,
    text="Pepsi",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
pepsiLabel.grid(row=1, column=0, padx=8, pady=8, sticky="w")

pepsiEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
pepsiEntry.grid(row=1, column=1, padx=8, pady=8)

spriteLabel = Label(
    coolDrinkFrame,
    text="Sprite",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
spriteLabel.grid(sticky="w", row=2, column=0, padx=8, pady=8)

spriteEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
spriteEntry.grid(row=2, column=1, padx=8, pady=8, sticky="w")

dewLabel = Label(
    coolDrinkFrame,
    text="Dew",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
dewLabel.grid(sticky="w", row=3, column=0, padx=8, pady=8)

dewEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
dewEntry.grid(row=3, column=1, padx=8, pady=8)

frootiLabel = Label(
    coolDrinkFrame,
    text="Frooti",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
frootiLabel.grid(sticky="w", row=4, column=0, padx=8, pady=8)

frootiEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
frootiEntry.grid(row=4, column=1, padx=8, pady=8)

cocaColaLabel = Label(
    coolDrinkFrame,
    text="Coca Cola",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
cocaColaLabel.grid(sticky="w", row=5, column=0, padx=8, pady=8)

cocaColaEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
cocaColaEntry.grid(row=5, column=1, padx=8, pady=8)

# Bill Frame

billFrame = Frame(productFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=10)

billAreaLabel = Label(
    billFrame,
    text="Bill Area",
    font=("times new roman", 15, "bold"),
    bd=7,
    relief=GROOVE,
)
billAreaLabel.pack(fill=X)

# scroll bar
scrollbar = Scrollbar(billFrame, orient=VERTICAL)
# orient is for we want horizontal or vertical scroll bars
scrollbar.pack(side=RIGHT, fill=Y)

textArea = Text(billFrame, height=19, width=55, yscrollcommand=scrollbar.set)
# yscrollcommand is to move the scrollbar automatically along with content

textArea.pack()
scrollbar.config(command=textArea.yview)
# the above is for upward movement for scrollbar when content is present
root.mainloop()  # for window continuously showing
