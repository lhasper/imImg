import os
import requests
from PIL import Image
from io import BytesIO

def download_and_convert_image(url, save_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Open the image using PIL
        image = Image.open(BytesIO(response.content))

        # Resize the image to 175x175 pixels
        image = image.resize((175, 175))

        # Extract the base file name from the URL and change the extension to .webp
        base_name = os.path.splitext(url.split("/")[-1])[0]
        full_path = os.path.join(save_path, f"{base_name}.webp")

        # Save the image as .webp
        image.save(full_path, format='WEBP')

        print(f"Image successfully downloaded, resized, converted, and saved to {full_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image from {url}: {e}")
    except Exception as e:
        print(f"Error processing the image from {url}: {e}")


if __name__ == "__main__":
    # Array of image URLs to be downloaded
    image_urls = [
        "https://go-upc.com/barcode/072549000667",
"https://go-upc.com/barcode/080833101242",
"https://go-upc.com/barcode/080833100122",
"https://go-upc.com/barcode/041798002104",
"https://go-upc.com/barcode/041798002258",
"https://go-upc.com/barcode/041798002401",
"https://go-upc.com/barcode/041798002951",
"https://go-upc.com/barcode/041798004351",
"https://go-upc.com/barcode/689076548380",
"https://go-upc.com/barcode/893007002050",
"https://go-upc.com/barcode/893007002098",
"https://go-upc.com/barcode/893007002128",
"https://go-upc.com/barcode/893007002029",
"https://go-upc.com/barcode/073731001219",
"https://go-upc.com/barcode/073731002353",
"https://go-upc.com/barcode/073731002742",
"https://go-upc.com/barcode/073731002902",
"https://go-upc.com/barcode/073731002919",
"https://go-upc.com/barcode/073731004159",
"https://go-upc.com/barcode/073731004197",
"https://go-upc.com/barcode/073731008300",
"https://go-upc.com/barcode/073731070000",
"https://go-upc.com/barcode/073731070130",
"https://go-upc.com/barcode/073731070147",
"https://go-upc.com/barcode/073731071076",
"https://go-upc.com/barcode/073731071090",
"https://go-upc.com/barcode/073731071212",
"https://go-upc.com/barcode/073731071403",
"https://go-upc.com/barcode/073731071502",
"https://go-upc.com/barcode/073731071519",
"https://go-upc.com/barcode/073731071564",
"https://go-upc.com/barcode/073731071588",
"https://go-upc.com/barcode/073731071595",
"https://go-upc.com/barcode/073731071601",
"https://go-upc.com/barcode/073731071625",
"https://go-upc.com/barcode/073731071700",
"https://go-upc.com/barcode/073731071717",
"https://go-upc.com/barcode/073731072004",
"https://go-upc.com/barcode/073731200056",
"https://go-upc.com/barcode/073731990506",
"https://go-upc.com/barcode/860062002226",
"https://go-upc.com/barcode/713733223096",
"https://go-upc.com/barcode/719283328229",
"https://go-upc.com/barcode/713733008334",
"https://go-upc.com/barcode/713733008341",
"https://go-upc.com/barcode/713733008358",
"https://go-upc.com/barcode/713733008389",
"https://go-upc.com/barcode/713733008396",
"https://go-upc.com/barcode/713733008426",
"https://go-upc.com/barcode/041250009450",
"https://go-upc.com/barcode/041250011811",
"https://go-upc.com/barcode/041250011828",
"https://go-upc.com/barcode/041250011835",
"https://go-upc.com/barcode/708820030381",
"https://go-upc.com/barcode/708820030558",
"https://go-upc.com/barcode/708820030589",
"https://go-upc.com/barcode/708820040243",
"https://go-upc.com/barcode/713733056854",
"https://go-upc.com/barcode/713733064866",
"https://go-upc.com/barcode/041250066859",
"https://go-upc.com/barcode/713733068369",
"https://go-upc.com/barcode/713733068567",
"https://go-upc.com/barcode/713733068574",
"https://go-upc.com/barcode/713733068581",
"https://go-upc.com/barcode/041250073437",
"https://go-upc.com/barcode/041250073444",
"https://go-upc.com/barcode/041250087694",
"https://go-upc.com/barcode/041250087700",
"https://go-upc.com/barcode/041250087786",
"https://go-upc.com/barcode/041250087793",
"https://go-upc.com/barcode/041250087809",
"https://go-upc.com/barcode/708820115217",
"https://go-upc.com/barcode/713733124065",
"https://go-upc.com/barcode/713733124072",
"https://go-upc.com/barcode/713733124089",
"https://go-upc.com/barcode/760236125211",
"https://go-upc.com/barcode/760236125235",
"https://go-upc.com/barcode/760236125242",
"https://go-upc.com/barcode/760236125259",
"https://go-upc.com/barcode/760236125273",
"https://go-upc.com/barcode/760236125310",
"https://go-upc.com/barcode/760236125341",
"https://go-upc.com/barcode/760236125365",
"https://go-upc.com/barcode/760236125372",
"https://go-upc.com/barcode/760236150596",
"https://go-upc.com/barcode/760236150664",
"https://go-upc.com/barcode/760236161882",
"https://go-upc.com/barcode/708820176058",
"https://go-upc.com/barcode/708820176102",
"https://go-upc.com/barcode/713733286558",
"https://go-upc.com/barcode/713733286565",
"https://go-upc.com/barcode/713733286572",
"https://go-upc.com/barcode/713733286596",
"https://go-upc.com/barcode/886926296594",
"https://go-upc.com/barcode/708820318281",
"https://go-upc.com/barcode/708820318779",
"https://go-upc.com/barcode/708820320574",
"https://go-upc.com/barcode/708820320710",
"https://go-upc.com/barcode/719283328069",
"https://go-upc.com/barcode/719283328083",
"https://go-upc.com/barcode/719283328212",
"https://go-upc.com/barcode/708820343795",
"https://go-upc.com/barcode/708820353183",
"https://go-upc.com/barcode/760236364474",
"https://go-upc.com/barcode/708820364851",
"https://go-upc.com/barcode/886926377583",
"https://go-upc.com/barcode/886926377590",
"https://go-upc.com/barcode/896180001001",
"https://go-upc.com/barcode/896180001018",
"https://go-upc.com/barcode/896180001025",
"https://go-upc.com/barcode/896180001032",
"https://go-upc.com/barcode/896180001100",
"https://go-upc.com/barcode/896180001292",
"https://go-upc.com/barcode/896180001704",
"https://go-upc.com/barcode/896180001773",
"https://go-upc.com/barcode/896180001568",
"https://go-upc.com/barcode/079746200005",
"https://go-upc.com/barcode/079746230002",
"https://go-upc.com/barcode/079746300002",
"https://go-upc.com/barcode/079746220003",
"https://go-upc.com/barcode/850030745880",
"https://go-upc.com/barcode/850030745897",
"https://go-upc.com/barcode/860002461755",
"https://go-upc.com/barcode/860451000406",
"https://go-upc.com/barcode/860451000413",
"https://go-upc.com/barcode/850003748771",
"https://go-upc.com/barcode/850003748788",
"https://go-upc.com/barcode/850003748795",
"https://go-upc.com/barcode/850003748832",
"https://go-upc.com/barcode/850003748856",
"https://go-upc.com/barcode/850003748870",
"https://go-upc.com/barcode/850003748887",
"https://go-upc.com/barcode/041953001805",
"https://go-upc.com/barcode/041953001829",
"https://go-upc.com/barcode/041953001843",
"https://go-upc.com/barcode/041953001928",
"https://go-upc.com/barcode/041953001942",
"https://go-upc.com/barcode/041953002772",
"https://go-upc.com/barcode/041953003540",
"https://go-upc.com/barcode/041953004370",
"https://go-upc.com/barcode/041953004400",
"https://go-upc.com/barcode/041953014508",
"https://go-upc.com/barcode/041953003946",
"https://go-upc.com/barcode/041953003953",
"https://go-upc.com/barcode/041953075059",
"https://go-upc.com/barcode/041953075066",
"https://go-upc.com/barcode/041953075073",
"https://go-upc.com/barcode/041953075080",
"https://go-upc.com/barcode/015500183689",
"https://go-upc.com/barcode/015500183764",
"https://go-upc.com/barcode/015500191356",
"https://go-upc.com/barcode/815099021634",
"https://go-upc.com/barcode/815099021641",
"https://go-upc.com/barcode/815099021658",
"https://go-upc.com/barcode/815099021665",
"https://go-upc.com/barcode/815099021672",
"https://go-upc.com/barcode/815099021689",
"https://go-upc.com/barcode/815099021696",
"https://go-upc.com/barcode/815099021726",
"https://go-upc.com/barcode/815099021801",
"https://go-upc.com/barcode/815099021900",
"https://go-upc.com/barcode/815099021788",
"https://go-upc.com/barcode/815099021795",
"https://go-upc.com/barcode/815099021832",
"https://go-upc.com/barcode/815099021849",
"https://go-upc.com/barcode/815099022181",
"https://go-upc.com/barcode/815099022204",
"https://go-upc.com/barcode/078858521442",
"https://go-upc.com/barcode/078858525051",
"https://go-upc.com/barcode/078858540009",
"https://go-upc.com/barcode/078858540047",
"https://go-upc.com/barcode/029243000011",
"https://go-upc.com/barcode/029243000028",
"https://go-upc.com/barcode/029243000059",
"https://go-upc.com/barcode/029243000066",
"https://go-upc.com/barcode/029243000073",
"https://go-upc.com/barcode/029243000080",
"https://go-upc.com/barcode/029243000103",
"https://go-upc.com/barcode/029243000127",
"https://go-upc.com/barcode/029243000134",
"https://go-upc.com/barcode/029243000233",
"https://go-upc.com/barcode/029243000240",
"https://go-upc.com/barcode/029243005009",
"https://go-upc.com/barcode/739478505600",
"https://go-upc.com/barcode/041953004288",
"https://go-upc.com/barcode/048564067008",
"https://go-upc.com/barcode/048564070022",
"https://go-upc.com/barcode/048564072057",
"https://go-upc.com/barcode/048564074037",
"https://go-upc.com/barcode/048564060023",
"https://go-upc.com/barcode/713733279482",
"https://go-upc.com/barcode/814026008120",
"https://go-upc.com/barcode/814026008144",
"https://go-upc.com/barcode/814026008168",
"https://go-upc.com/barcode/814026009820",
"https://go-upc.com/barcode/865957000165",
"https://go-upc.com/barcode/094922522535",
"https://go-upc.com/barcode/708820030510",
"https://go-upc.com/barcode/708820030572",
"https://go-upc.com/barcode/708820051942",
"https://go-upc.com/barcode/708820052338",
"https://go-upc.com/barcode/708820062580",
"https://go-upc.com/barcode/708820176072",
"https://go-upc.com/barcode/708820176096",
"https://go-upc.com/barcode/708820178311",
"https://go-upc.com/barcode/708820263314",
"https://go-upc.com/barcode/708820279957",
"https://go-upc.com/barcode/708820320703",
"https://go-upc.com/barcode/713733008365",
"https://go-upc.com/barcode/713733056847",
"https://go-upc.com/barcode/713733224857",
"https://go-upc.com/barcode/713733224864",
"https://go-upc.com/barcode/713733224871",
"https://go-upc.com/barcode/719283328090",
"https://go-upc.com/barcode/719283557346",
"https://go-upc.com/barcode/719283592989",
"https://go-upc.com/barcode/760236125204",
"https://go-upc.com/barcode/760236125228",
"https://go-upc.com/barcode/760236125266",
"https://go-upc.com/barcode/760236125358",
"https://go-upc.com/barcode/760236150572",
"https://go-upc.com/barcode/760236150602",
"https://go-upc.com/barcode/760236150701",
"https://go-upc.com/barcode/760236150718",
"https://go-upc.com/barcode/760236152514",
"https://go-upc.com/barcode/760236152521",
"https://go-upc.com/barcode/760236152538",
"https://go-upc.com/barcode/760236161400",
"https://go-upc.com/barcode/886926377569",
"https://go-upc.com/barcode/886926377576"
        # Add more URLs as needed
    ]

    # Directory where the images will be saved
    save_directory = r"C:\Cont\Python Projects\BarcodeImage"

    # Ensure the save directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Download each image
    for image_url in image_urls:
        download_and_convert_image(image_url, save_directory)
