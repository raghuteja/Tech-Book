# Collaborative Editing

### Strategies

#### Locking

A shared document may only be edited by one user at a time and others will have read only access to that document (Realtime collaboration is not possible)

One improvement for this can be dynamically add and release locks for subsections of the document (Still realtime collaboration problem is not completely solved)
    
#### Event Passing

Capture all users actions and mirroring them across the network to other users (If one event gets lost then the documents can be divergent)

Three way merges similar to subversion, Client sends data to server and server performs a three-way merge to extract the user's changes and merge them with changes from other users (What happens when user modifies document while three way merge is going on)
    
#### Differential Synchronization

It is based on diff and patch operations


    
### Credits

1. [Complete credits to Neil Fraser (Author of Differential Synchronization)](https://neil.fraser.name/writing/sync/), Content and images are taken from https://neil.fraser.name/