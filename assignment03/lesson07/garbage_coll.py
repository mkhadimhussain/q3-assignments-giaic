# Agentic AI - Python - Lesson 07 - The Set, Frozenset & GC

# GC: Garbage Collection
# Python has a garbage collection mechanism.

# Python's garbage collector is a Memory Management System that automatically frees up memory occupied 
# by objects that are no longer needed or referenced. This helps prevent memory leaks and allows Python 
# to manage memory efficiently.

# Here's how it works:
# 1- Reference Counting: Python uses a reference counting algorithm to track the number of references to 
#    each object. When an object is created, its reference count is set to 1. Each time a new reference to 
#    the object is created (e.g., assigning it to a variable or passing it as an argument), the reference 
#    count is incremented.

# 2- Garbage Collection: When an object's reference count reaches 0, it is no longer needed and becomes 
#    eligible for garbage collection. The garbage collector periodically runs in the background to identify 
#    and free up memory occupied by these objects.

#--------------------------------------------------------------------------------------------------

# Python's garbage collector is:

# - Automatic: You don't need to manually manage memory or explicitly free up memory.
# - Periodic: The garbage collector runs periodically to clean up memory.
# - Reference-based: It uses reference counting to determine which objects are no longer needed.

#--------------------------------------------------------------------------------------------------

# You can also manually trigger the garbage collector using the gc.collect() function from the gc module:

import gc

gc.collect()
print(gc.get_count()) # prints the number of collected objects, unreachable objects, and reference cycles
# (0, 0, 0)

#--------------------------------------------------------------------------------------------------

# However, this is usually not necessary, as the garbage collector runs automatically in the background.

# Some benefits of Python's garbage collection:

# - Memory safety: Prevents memory leaks and ensures memory is freed up when no longer needed.
# - Convenience: You don't need to worry about manually managing memory.
# - Efficiency: The garbage collector runs periodically to optimize memory usage.

# Note that Python's garbage collection is not perfect, and there are some cases where it may not work as 
# expected (e.g., circular references, file descriptors). However, it provides a convenient and efficient 
# way to manage memory in most cases.

#--------------------------------------------------------------------------------------------------
