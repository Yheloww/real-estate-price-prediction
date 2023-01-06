from get_links import * 


def pool(numbers_drivers, pages):
    # 1 driver by thread (we have four thread here)
    drivers = [driver_gen() for _ in range(numbers_drivers)]
    #division of the number of pages by the number of threads 
    division = np.array_split(np.arange(1,pages),numbers_drivers)
    #creation of a pool of threads
    list_of_result = []
    with ThreadPoolExecutor(max_workers=numbers_drivers) as executor :
        #it is where it needs refinement
        results = executor.map(get_links,division,drivers)
        for result in results :
            for x in result : 
                #print(x)
                link_file(x)
            return 
            
pool(10,100)