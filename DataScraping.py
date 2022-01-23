#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import sys

cats = ["Affiliation and Relationships", "Physical Characteristics","Origin and Living Status","Personal Information","Creators and Appearances","Contents", "Categories"]


#returns the values between str and str2 in an array, with a fallback second string, which activates a trigger bool if reached
def inbetweener(str1, str2, arr, Fallback = None, trigger = None):
    vals =[]
    found = False;
    fallback = False;
    for line in arr:
        if (line == str1):
            found = True
        if (line == str2):
            found = False
        if (Fallback in line and found == True):
            found = False
            fallback = True
        if(found):
            vals.append(line)
    if(fallback):
        if(trigger != None):
            trigger.clear()
            trigger.append(True)
    return vals


#Scrape all the information that we are looking for at a given url
def Prelim_scrape (url):
    #print(url)
    
    try:
        req=requests.get(url)
        req.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(url + "failed\n")
        return
    except requests.exceptions.MissingSchema as err:
        print(url + " does not exist")
        return
    except requests.exceptions.InvalidSchema:
        print(url + " does not exist")
        return
    #handle various states that could cause this url to be invalid and error out.
    content=req.text
    html=BeautifulSoup(content)
    simple_text = [line for line in html.get_text().split('\n') if line.strip() != '']
    out = []
    flag = [False]
    #try to get the info in these specific sections, which are consistient across the site.
    out.append(inbetweener("Affiliation and Relationships", "Physical Characteristics", simple_text, "Contents", flag))
    if(flag[0]):
        out[-1] = inbetweener("Affiliation and Relationships","Origin and Living Status", out[-1],  "Contents")
        flag = [False]
    out.append(inbetweener("Physical Characteristics","Origin and Living Status", simple_text,  "Contents", flag))
    if(flag[0]):
        out[-1] = inbetweener("Physical Characteristics","Personal Information", out[-1],  "Contents")
        flag = [False]
    out.append(inbetweener("Origin and Living Status","Personal Information", simple_text,  "Contents", flag))
    if(flag[0]):
        out[-1] = inbetweener("Origin and Living Status","Creators and Appearances", out[-1],  "Contents")
        flag = [False]
    out.append(inbetweener("Personal Information", "Creators and Appearances", simple_text,  "Creators and Appearances", flag))
    if(flag[0]):
        out[-1] = inbetweener("Personal Information","Contents", out[-1],  "Contents")
        flag = [False]
    out.append(inbetweener("Creators and Appearances", "Contents", simple_text,  "Contents", flag))
    out.append(inbetweener("Categories", "\t\tCommunity content is available under CC-BY-SA unless otherwise noted.\t", simple_text, "\t\t\t\t\t\t\tExplore Wikis\t\t\t\t\t\t", flag))
    return out

#function that takes a site, a dictionary and a limit to how many times let it has to recurse before it runs into pythons recursion threshold and attemps to scrape the site and then call itself on all the urls found on that site. 
def scrape(site, d, lim):
    print(lim)
    if(lim >= 900):
        return
    # getting the request from url
    try:
        r=requests.get(site)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        #print(url + " failed")
        return
    except requests.exceptions.MissingSchema:
        #print(url + " does not exist")
        return
    except requests.exceptions.InvalidSchema:
        #print(url + " does not exist")
        return
    
    # converting the text
    s = BeautifulSoup(r.text)
    original_stdout = sys.stdout
    name = site.split('/')[-1] + "_output.txt"
    #we don't want to make output files for category files, but we do want to use them for recursion
    if( "Category:" not in site):
        with open(name, 'a+') as f:
            sys.stdout = f
            for line in Prelim_scrape(site):
                for bit in line:
                    if bit in cats:
                        print('\t', end = '')
                    else:
                        print(bit, end = ',')

            f.close()
        sys.stdout =    original_stdout 
    
    d[site] = "Found"
    links = s.find_all('a')

    for tag in links:
        link = tag.get('href',None)
        onsite = True
        if(link is not None):
            if "marvel.fandom.com" not in link:
                link = "https://marvel.fandom.com" + str(link)
            if ".com" in link: 
                if "marvel.fandom.com/wiki/" in link:
                    onsite = True
                else:
                    onsite = False
        #all of these if statements are types of pages that either cause problems with the parser or are unwanted. Many were only found have hours of running the script. ? or generated html pages were a particular problem            
        if ((link is not None) and (not str(link) in d) and ("/wiki/" in link) and ("Special:" not in link) and ("Hub:" not in link) and ("Marvel_Database" not in link) and ("Help:" not in link) and ("mobile" not in link) and onsite and ("Talk:" not in link) and ("User:" not in link) and ("Message_Wall:" not in link) and ("Glossary:" not in link) and ("?" not in link) and ("Category_talk:" not in link)):
            print(link)
            #print(str(site) + "\n")
            # calling it self
            if(lim >= 900):
                return
            scrape(link, d, lim + 1)


# In[ ]:

#run the script on the first argument given
urls={}
recursionLimit = 0
scrape(sys.argv[1], urls, recursionLimit)
original_stdout = sys.stdout
print(urls)
    


# In[ ]:




