### process_pool.py
Process pools are helpful for speeding up the python data processing scripts.

**Steps :**
1. import the concurrent.futures library.
2. tell Python to boot up 4 extra Python instances(for 4 core) using `with concurrent.futures.ProcessPoolExecutor() as executor:`
3. initial step is to ask the Process Pool to execute our helper function on our list of data using those 4 processes using `executor.map():`

**When to use :**
- Grabbing statistics out of a collection of separate web server log files
- Parsing data out of a bunch of XML, CSV or json files
- Pre-processing lots of images to create a machine learning data set