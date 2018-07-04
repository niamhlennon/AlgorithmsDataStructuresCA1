'''
__author__ = Ken Brown, University College Cork
__date__ =
__course__ = 

'''

''' DLLNODE CLASS '''

class DLLNode:

# Constructor
    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode


# String Magic Method
    def __str__(self):
        return self.element._name




''' DLL CLASS '''
 
class DLL:

# Constructor
    def __init__(self):
                          # item, prevnode, nextnode
        self._head = DLLNode(None, None, None) 
        self._tail = DLLNode(None, self._head, None) 
        self._head.next = self._tail 
        self._size = 0



# Getters

    def get_first(self):
        return self._head.next

    def get_last(self):
        return self._tail.prev



# Doubly Linked Lists Methods

    def add_after(self, item, before):
        # adds a new node with item as its element after the node before
        after = before.next
        insert = DLLNode(item, before, after)
        insert.prev = before
        insert.next = after
        insert.next.prev = insert
        before.next = insert
        self._size += 1
        return insert
                
    def add_first(self, item):
        # adds to the beginning of the list, after the head
        add_after(item, self._head)

    def add_last(self, item):
        # adds to the end of the list, before the tail
        add_after(item, self._tail.prev)
        
    def remove_node(self, node):
        # removes node specified, from anywhere in the list
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        node.prev = None
        node.next = None
        node.element = None
        self._size -= 1

    def remove_first(self):
        # removes the first node, excluding the head
        remove_node(self._head.next)

    def remove_last(self):
        # removes the last node, excluding the tail
        remove_node(self._tail.prev)

    def get_size(self):
        # return the size of the list
        return self._size

    def is_empty(self):
        # checks if the list is empty
        return self._size == 0



# String Magic Method

    def __str__(self):
        node = self._head.next
        allnodes = ""
        while node.next is not None:
            allnodes += str(node) + ", "
            node = node.next
        return allnodes

        

''' MOVIE CLASS '''   


class Movie:


# Constructor

    def __init__(self, name, director, dateadded, viewed):
        self._name = name
        self._director = director
        self._dateadded = dateadded
        self._viewed = viewed



# Play Method

    def play(self):
        # plays currently selected movie
        self._viewed = True
        print(self, "\n")

# Getters and Setters

    def getTitle(self):
        return self._name

    def setTitle(self, name):
        self._name = name


    def getViewed(self):
        return self._viewed 
    
    def setViewed(self, viewed):
        self._viewed = viewed        

    def getDirector(self):
        return self._director

    def setDirector(self, director):
        self._director = director

    def getDateAdded(self):
        return self._dateadded 
    
    def setDateAdded(self, dateadded):
        self._dateadded = dateadded

  
# String Magic Method

    def __str__(self):     
        return("%s %s %i %s" % (self._name, self._director, self._dateadded, self._viewed))



    
''' FLIXNETLIBRARY CLASS '''


class FlixNetLibrary:

# Constructor
    def __init__(self):
        self._movies = DLL()
        self._current = self._movies._head


# Flixnet Library Methods

    def add_movie(self, movie):
        # adds a new movie to the library in decreasing order of dateadded
        newmovie = ""
        if self._movies.get_size() == 0:
            newmovie = self._movies.add_after(movie, self._movies._head)
            return newmovie
        else:
            node = self._movies._head.next
            while node is not self._movies._tail: 
                if node.element._dateadded < movie._dateadded:
                    newmovie = self._movies.add_after(movie, node.prev) 
                    break
                else:
                    node = node.next                
            else: 
                newmovie = self._movies.add_after(movie, self._movies._tail.prev)
            return newmovie
                      
    
    def get_current(self):
        # displays the currently selected movie info
        if self._current not in [self._movies._head, self._movies._tail, None]:
            print("Current movie: %s \n" % self._current)


    def next_movie(self):
        # changes the current selection to the next one
        if self._current == self._movies._tail.prev or \
        self._current == self._movies._tail: 
            self._current = self._movies._head.next
        else:
            self._current = self._current.next

    def prev_movie(self):
        # changes the current selection to the previous one
        if self._current == self._movies._head.next or \
        self._current == self._movies._head: 
            self._current = self._movies._tail.prev
        else:
            self._current = self._current.prev
    
    def reset(self):
        # resets the current movie to the list head
        self._current = self._movies._head

    
    def play(self):
        # plays currently selected movie and outputs the movie title being played
        # calls the Movie's play method
        if self._current in [self._movies._head, self._movies._tail, None]:
            return
        print("Currently playing: ", end="") 
        self._current.element.play()

    
    def remove_current(self):
        if self._current in [self._movies._head, self._movies._tail, None]:
            return
        # removes the current movie from the directory
        if self._current == self._movies._tail.prev:
            newcurrent = self._movies._head
        else:
            newcurrent = self._current.next

        self._movies.remove_node(self._current)
        
        self._current = newcurrent


    def length(self):
        # reports the number of movies
        return self._movies.get_size()


    ''' PART 4 - SEARCHING FOR SUBSTRING '''

    def search_sub(self, substring):
        # search the movie directory for a given substring in either the movie or director fields
        # set the movie to the current movie if found, otherwise return false
        node = self._current
        if node in [self._movies._head, self._movies._tail, None]:
            return False
        while True:
            if substring.lower() in node.element._name.lower() or \
            substring.lower() in node.element._director.lower():
                self._current = node 
                return
            else:
                if node.next == self._movies._tail:
                    node = self._movies._head.next
                else:
                    node = node.next
                if node == self._current: 
                    return False      

# String Magic Method     

    def __str__(self):
        movies = ""
        node = self._movies._head.next
        while node != self._movies._tail:
            movies += node.element.__str__() + "\n" 
            node = node.next
        return("%s" % (movies))


''' TEST CODE '''


if __name__ == '__main__':   

# Flixnet Testing

    # create empty library
    flix = FlixNetLibrary()

    # create 3 movie instances
    movie1 = Movie("Bladerunner 2049", "Villeneuve", 20171004, False)
    movie2 = Movie("Hail, Caesar!", "Coen & Coen", 20160304, False)
    movie3 = Movie("Wonder Woman", "Jenkins", 20170601, False)
    flix.add_movie(movie1)
    flix.add_movie(movie2)
    flix.add_movie(movie3)

    # check length
    size = flix.length()
    print(size)

    # display library to screen
    print(flix)

    # set current movie to be the next one
    flix.next_movie()

    # play current movie
    flix.play()

    # move current movie to the next one
    flix.next_movie()

    # report the current movie
    flix.get_current()

    # move the current movie to the previous movie
    flix.prev_movie()

    # delete the current movie
    flix.remove_current()

    # check length after movie removed
    size = flix.length()
    print(size)

    # display the library to screen
    print(flix)

    # create new instance of movie
    movie4 = Movie("The Imitation Game", "Tyldum", 20141114, False)
    flix.add_movie(movie4)

    # check length after 
    size = flix.length()
    print(size)
    
    # move current to the next movie
    flix.next_movie()

    # play current movie
    flix.play()

    # display the library to screen
    print(flix)

    # checks substring search method
    flix.search_sub("imi")
    flix.get_current()

    # reset test
    flix.reset()
    print(flix)

    # wrap around test
    flix.next_movie()
    flix.get_current()
    flix.prev_movie()
    flix.get_current()
    flix.next_movie()
    flix.get_current()


# Movie Testing

    # add movie test
    movie5 = Movie("Rouge One", "Efwards", 30161210, False)
    print(movie5)

    # getters and setters test
    movie5.setTitle("Rogue One")
    movie5.getTitle()
    print(movie5)

    movie5.setDirector("Edwards")
    movie5.getDirector()
    print(movie5)

    movie5.setDateAdded(20161210)
    movie5.getDateAdded()
    print(movie5)

    movie5.setViewed(True)
    movie5.getViewed()
    print(movie5)

    # play method test
    movie5.play()


    
