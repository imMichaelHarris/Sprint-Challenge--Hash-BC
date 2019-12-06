#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        # hash_table_remove,
                        hash_table_retrieve,
                        # hash_table_resize
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # index = 0
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)


        # What other weight do we need to match the limit?

    for i in range(len(weights)):
        other_weight = limit - weights[i]
        if hash_table_retrieve(ht, other_weight):
            # Find higher value
            weight_index = hash_table_retrieve(ht, other_weight)
            print("tuple", hash_table_retrieve(ht, other_weight), i)
            return (weight_index, i)
            # if weight_index > hash_table_retrieve(ht, weight):
            #     return (weight_index, hash_table_retrieve(ht, weight))
            # else:
            #     print("Other",hash_table_retrieve(ht, weight), weight_index )
            #     return (hash_table_retrieve(ht, weight), weight_index)
        # else:
        #     return None




def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
        return answer[0], answer[1]
    else:
        print("None")
