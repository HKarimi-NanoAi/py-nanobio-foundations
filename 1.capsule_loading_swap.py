#____________________________________________________________________________________________________________________________________
# Topic = Variable Swapping in Polymeric Nanocapsules Data
# Description: Demonstrating Python's clean syntax for swapping values between two variables without using a temporary variable.
# Application: Useful for re-indexing or re-ordering experimental groups.
# This is only an example to show you how we can swap values
#____________________________________________________________________________________________________________________________________


capsule_1_loading = 85.5
capsule_2_loading = 42.1
capsule_1_loading , capsule_2_loading = capsule_2_loading , capsule_1_loading
