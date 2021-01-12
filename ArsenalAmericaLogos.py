#!/usr/bin/env python3
print("this is a test")
# import requests
# import lxml.html as lh
# import pandas as pd
# from PIL import Image
# from io import BytesIO

# def getLogosDF(url):
#     #Create a handle, page, to handle the contents of the website
#     page = requests.get(url)
#     #Store the contents of the website under doc
#     doc = lh.fromstring(page.content)
#     #Parse data that are stored between <tr>..</tr> of HTML
#     tr_elements = doc.xpath('//tr')

#     #tr_elements = [T for T in tr_elements_temp if len(T)>3]
#     #Remove ParentDirectory row and dummy row
#     tr_elements.pop(1)
#     tr_elements.pop(1)

#     #Create empty list
#     rows=[]

#     for T in tr_elements:
#         cols =[]
#         if len(T) == 5: #We only want complete rows
#             for t in T.iterchildren():
#                 cols.append(t.text_content())
#             rows.append(cols)
#     headers = rows.pop(0)

#     df = pd.DataFrame(rows, columns=headers)
#     dropcols = [0,3,4]
#     df.drop(df.columns[dropcols],axis=1,inplace=True)
#     df_orig = df[~df['Name'].str.contains("-", na=False)].reset_index(drop=True)
#     return(df_orig)

# def has_transparency(img):
#     if img.mode == "P":
#         transparent = img.info.get("transparency", -1)
#         for _, index in img.getcolors():
#             if index == transparent:
#                 return True
#     elif img.mode == "RGBA":
#         extrema = img.getextrema()
#         if extrema[3][0] < 255:
#             return True
#     return False

# def createMapLogos(url,df,background_img):
#     base_url = url
#     logos_list = df['Name'].tolist()
#     getbg = requests.get(background_img)
#     wp = 'https://www.arsenalamerica.com/wp-json/wp/v2/media'
#     # logos = [logo for logo in logos_list if logo.str.contains('.')]
#     for logo in logos_list:
#         if logo=='ForMap/':
#             continue
#         bg = Image.open(BytesIO(getbg.content))
#         logo_url = base_url + '/' + logo
#         response = requests.get(logo_url)
#         img = Image.open(BytesIO(response.content))
#         # print("{} \tis mode {}.".format(logo, has_transparency(img)))
#         fgx, fgy = img.size
#         if fgx > fgy:
#             new_fgx = 130
#             new_fgy = round(new_fgx * fgy / fgx)
#         else:
#             new_fgy = 130
#             new_fgx = round(new_fgy * fgx / fgy)
#         fg = img.resize((new_fgx, new_fgy), Image.ANTIALIAS).convert("RGBA")
#         x = round((130-new_fgx)/2)
#         bg.paste(fg, (x,0), fg)
#         print(logo)
#         # if has_transparency(fg):
#         #     bg.paste(fg, (x,0), fg)
#         # else:
#         #     bg.paste(fg, (x,0))
#         # bg.show()
#         bg.save('./logos/' + logo,"PNG")
#         # upload_url = self.__upload_media_url()
#         # with open('./templogo', 'r') as f:
#         #     f.show()
#             # headers = { "Content-Disposition": f"attachment; filename=test" , "Content-Type": "image/png" }
#             # requests.post(url=wp,
#             #     data=f,
#             #     headers=headers,
#             #     auth=('bryceglarsen@gmail.com', '#AFCUSA!886'))


# if __name__ == '__main__':
#     url='https://www.arsenalamerica.com/wp-content/uploads/BranchLogos/Static'
#     logos_df = getLogosDF(url)
#     background_img = 'https://www.arsenalamerica.com/wp-content/uploads/BranchLogos/Static/ForMap/WhiteBackground-130x130.jpg'
#     createMapLogos(url,logos_df,background_img)
