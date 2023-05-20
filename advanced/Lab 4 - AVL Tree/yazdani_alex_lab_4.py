"""
Lab 4: AVL Tree
Alexander Yazdani
CWID: 20399751
Date: 05/10/2023

This file inherits the Binary Search Tree Class from BST.py, and creates an
AVLTreeNode class and AVLTree class.
The AVLTree class adds methods for both left and right rotation, and will
self-balance upon node insertion and removal.
The test proram at the end of the file creates an AVL tree with 1000 random
nodes between 0-1000, then removes the majority of the tree, then adds in 50
more nodes, 1000-1049.  Every step of the way, it is shown that the AVL depth
condition is met.
"""
import random
from treelib import Tree
from BST import BinaryTreeNode, BinarySearchTree


class AVLTreeNode(BinaryTreeNode):
    """
    Class specific to AVL Tree Nodes
    """

    def __init__(self, data):
        """
        Initialize an AVL Tree Node, inherited from BinaryTreeNode
        """
        self.height = 0
        super().__init__(data)

    def calc_height(self):
        """
        Function to calcualte a node's height based on child heights.
        """
        self.height = max(self.child_heights) + 1

    @property
    def child_heights(self):
        """
        Function to find child heights of a given node.
        """
        if self.left_child is None:
            left_height = -1
        else:
            left_height = self.left_child.height
        if self.right_child is None:
            right_height = -1
        else:
            right_height = self.right_child.height
        return left_height, right_height


class AVLTree(BinarySearchTree):
    """
    Class specific to AVL Trees
    """

    def calc_heights_after_rotation(self, new_sub_root):
        """
        Function to reassess the height of child nodes after a rotation.
        """
        if new_sub_root.left_child is not None:
            new_sub_root.left_child.calc_height()
        if new_sub_root.right_child is not None:
            new_sub_root.right_child.calc_height()
        new_sub_root.calc_height()

    def right_rotation(self, sub_root):
        """
        Function to perform a single right rotation.
        """
        new_sub_root = sub_root.left_child
        intermediate_child = new_sub_root.right_child
        new_sub_root.right_child = sub_root
        new_sub_root.right_child.left_child = intermediate_child
        self.calc_heights_after_rotation(new_sub_root)
        return new_sub_root

    def left_rotation(self, sub_root):
        """
        Function to perform a single left rotation.
        """
        new_sub_root = sub_root.right_child
        intermediate_child = new_sub_root.left_child
        new_sub_root.left_child = sub_root
        new_sub_root.left_child.right_child = intermediate_child
        self.calc_heights_after_rotation(new_sub_root)
        return new_sub_root

    def _insert(self, data, sub_root):
        """
        Insert a node into the AVL tree.
        """
        if sub_root is None:
            self._size += 1
            return AVLTreeNode(data)
        sub_root = super()._insert(data, sub_root)
        sub_root = self._rotate_if_needed(sub_root)
        return sub_root

    def _remove(self, data, sub_root):
        """
        Remove a node from the AVL tree.
        """
        sub_root = super()._remove(data, sub_root)
        sub_root = self._rotate_if_needed(sub_root)
        return sub_root

    def _rotate_if_needed(self, node):
        """
        Function to check if rotation is needed, both single and double.
        """
        if node is None:
            return node
        node.calc_height()
        (left_height, right_height) = node.child_heights
        if left_height - right_height > 1:
            # Right Rotation Needed
            if node.left_child is not None:
                (left_height, right_height) = \
                    node.left_child.child_heights
                if right_height - left_height > 0:
                    # Left Right Rotation Needed
                    node.left_child = self.left_rotation(node.left_child)
            node = self.right_rotation(node)
        elif right_height - left_height > 1:
            # Left Rotation Needed
            if node.right_child is not None:
                (left_height, right_height) = \
                    node.right_child.child_heights
                if left_height - right_height > 0:
                    # Right Left Rotation Needed
                    node.right_child = self.right_rotation(node.right_child)
            node = self.left_rotation(node)
        return node

    def print_tree(self, sub_root=None):
        """
        function to print/display input tree
        """
        if sub_root is None:
            if self._root is None:
                return
            else:
                sub_root = self._root
        self._print_tree(sub_root, 0)

    def _print_tree(self, sub_root, depth):
        if sub_root is None:
            return
        for _ in range(depth):
            print("-", end="")
        print(sub_root.data)
        print("L")
        self._print_tree(sub_root.left_child, depth + 1)
        print("R")
        self._print_tree(sub_root.right_child, depth + 1)

    def show_tree(self):
        """
        Function that uses treelib to display trees.
        This function should make the input tree more readable that print_tree() method.
        """
        def form_tree(child, parent=None):
            if child is self._root:
                visual_tree.create_node(tag=child.data, identifier=child)
            else:
                visual_tree.create_node(tag=child.data, identifier=child, parent=parent)
        visual_tree = Tree()
        self.traverse_tree(form_tree)
        visual_tree.show(reverse=True, line_type='ascii-ex')
        # visual_tree.save2file(filename='my_tree.txt', reverse=True, line_type='ascii-ex')


def check_AVL_cond(sub_root):
    """
    Function to check if AVL condition is met.
    """
    if sub_root is not None:
        (left, right) = sub_root.child_heights
        if abs(left-right) > 1:
            print("AVL Violated")
        if sub_root.left_child is not None:
            check_AVL_cond(sub_root.left_child)
        if sub_root.right_child is not None:
            check_AVL_cond(sub_root.right_child)


def main():
    """
    The main() function acts as a test program for the AVLTree and AVLTreeNode
    classes.
    First, an AVL tree is created by inserting 500 random numbers between 0
    and 1000.
    The Tree is then displayed, and it can be seen that the depth condition of
    AVL is not violated.
    Next, 3000 random numbers between 0 and 1000 are removed, maing the new
    tree much smaller.
    The tree is displayed again and it can be seen that AVL is still not
    violated.
    Finally, numbers 1000 - 1049 are injected to make the tree lopsided, but
    printing the tree shows
    that AVL condition is still met.
    In addition, check_AVL_cond() is run for every insertion and removal,
    showing that AVL has not been violated at any step.
    """
    my_tree = AVLTree()
    random.seed(1)
    for _ in range(500):
        num = random.randint(0, 1000)
        # print("inserting", num)
        my_tree.insert(num)
        check_AVL_cond(my_tree._root)
    print("\nInitial Tree:")
    # my_tree.print_tree()
    my_tree.show_tree()

    for _ in range(3000):
        num = random.randint(0, 1000)
        # print("Removing", num)
        try:
            my_tree.remove(num)
            # print("Removed")

        except AVLTree.NotFoundError:
            pass
            # print("Not Found")
        check_AVL_cond(my_tree._root)

    print("\nNew Tree with Removed Numbers:")
    # my_tree.print_tree()
    my_tree.show_tree()
    
    for x in range(50):
        my_tree.insert(1000+x)
        check_AVL_cond(my_tree._root)
    print("\nNew Tree with Lopsided Injection:")
    my_tree.show_tree()

if __name__ == "__main__":
    """
    
    Initial Tree:
    582
    ├── 782
    │   ├── 867
    │   │   ├── 923
    │   │   │   ├── 967
    │   │   │   │   ├── 980
    │   │   │   │   │   ├── 992
    │   │   │   │   │   │   ├── 998
    │   │   │   │   │   │   │   ├── 1000
    │   │   │   │   │   │   │   │   └── 999
    │   │   │   │   │   │   │   └── 996
    │   │   │   │   │   │   │       └── 997
    │   │   │   │   │   │   └── 988
    │   │   │   │   │   │       ├── 990
    │   │   │   │   │   │       │   └── 991
    │   │   │   │   │   │       └── 982
    │   │   │   │   │   │           └── 985
    │   │   │   │   │   └── 975
    │   │   │   │   │       ├── 977
    │   │   │   │   │       └── 972
    │   │   │   │   │           └── 974
    │   │   │   │   └── 948
    │   │   │   │       ├── 961
    │   │   │   │       │   ├── 963
    │   │   │   │       │   │   └── 966
    │   │   │   │       │   └── 958
    │   │   │   │       │       ├── 960
    │   │   │   │       │       └── 953
    │   │   │   │       │           └── 954
    │   │   │   │       └── 938
    │   │   │   │           ├── 942
    │   │   │   │           │   ├── 944
    │   │   │   │           │   │   └── 947
    │   │   │   │           │   └── 939
    │   │   │   │           └── 932
    │   │   │   │               ├── 936
    │   │   │   │               └── 931
    │   │   │   └── 902
    │   │   │       ├── 914
    │   │   │       │   ├── 921
    │   │   │       │   │   ├── 922
    │   │   │       │   │   └── 917
    │   │   │       │   │       └── 918
    │   │   │       │   └── 907
    │   │   │       │       ├── 908
    │   │   │       │       │   └── 912
    │   │   │       │       └── 903
    │   │   │       └── 880
    │   │   │           ├── 890
    │   │   │           │   ├── 896
    │   │   │           │   │   ├── 899
    │   │   │           │   │   └── 892
    │   │   │           │   └── 886
    │   │   │           │       ├── 888
    │   │   │           │       └── 881
    │   │   │           └── 873
    │   │   │               ├── 878
    │   │   │               │   ├── 879
    │   │   │               │   └── 877
    │   │   │               └── 870
    │   │   │                   ├── 871
    │   │   │                   └── 868
    │   │   └── 821
    │   │       ├── 840
    │   │       │   ├── 855
    │   │       │   │   ├── 860
    │   │       │   │   │   ├── 866
    │   │       │   │   │   │   └── 861
    │   │       │   │   │   └── 857
    │   │       │   │   └── 849
    │   │       │   │       ├── 852
    │   │       │   │       └── 847
    │   │       │   │           └── 848
    │   │       │   └── 832
    │   │       │       ├── 836
    │   │       │       │   └── 839
    │   │       │       └── 823
    │   │       │           ├── 828
    │   │       │           │   └── 830
    │   │       │           └── 822
    │   │       └── 802
    │   │           ├── 807
    │   │           │   ├── 816
    │   │           │   │   ├── 817
    │   │           │   │   └── 815
    │   │           │   └── 805
    │   │           └── 794
    │   │               ├── 797
    │   │               │   ├── 800
    │   │               │   │   ├── 801
    │   │               │   │   └── 798
    │   │               │   └── 796
    │   │               └── 786
    │   │                   ├── 789
    │   │                   │   └── 788
    │   │                   └── 785
    │   └── 667
    │       ├── 712
    │       │   ├── 743
    │       │   │   ├── 760
    │       │   │   │   ├── 773
    │       │   │   │   │   ├── 779
    │       │   │   │   │   │   ├── 780
    │       │   │   │   │   │   └── 777
    │       │   │   │   │   └── 772
    │       │   │   │   │       └── 761
    │       │   │   │   └── 750
    │       │   │   │       ├── 755
    │       │   │   │       │   └── 758
    │       │   │   │       └── 746
    │       │   │   │           └── 747
    │       │   │   └── 728
    │       │   │       ├── 738
    │       │   │       │   ├── 741
    │       │   │       │   │   └── 742
    │       │   │       │   └── 736
    │       │   │       │       └── 732
    │       │   │       └── 720
    │       │   │           ├── 721
    │       │   │           └── 719
    │       │   └── 686
    │       │       ├── 693
    │       │       │   ├── 702
    │       │       │   │   ├── 711
    │       │       │   │   │   └── 703
    │       │       │   │   └── 694
    │       │       │   └── 690
    │       │       │       ├── 691
    │       │       │       └── 689
    │       │       └── 679
    │       │           ├── 680
    │       │           │   └── 681
    │       │           └── 675
    │       │               └── 672
    │       └── 644
    │           ├── 657
    │           │   ├── 663
    │           │   │   ├── 665
    │           │   │   │   └── 664
    │           │   │   └── 662
    │           │   └── 646
    │           │       ├── 650
    │           │       └── 645
    │           └── 603
    │               ├── 622
    │               │   ├── 629
    │               │   │   ├── 638
    │               │   │   │   ├── 639
    │               │   │   │   └── 637
    │               │   │   └── 626
    │               │   │       ├── 627
    │               │   │       └── 623
    │               │   └── 607
    │               │       ├── 618
    │               │       │   ├── 620
    │               │       │   └── 614
    │               │       └── 605
    │               │           └── 604
    │               └── 592
    │                   ├── 598
    │                   │   ├── 601
    │                   │   └── 593
    │                   └── 589
    │                       ├── 591
    │                       └── 584
    │                           ├── 587
    │                           └── 583
    └── 261
        ├── 460
        │   ├── 512
        │   │   ├── 540
        │   │   │   ├── 563
        │   │   │   │   ├── 569
        │   │   │   │   │   ├── 576
        │   │   │   │   │   │   ├── 578
        │   │   │   │   │   │   │   ├── 579
        │   │   │   │   │   │   │   └── 577
        │   │   │   │   │   │   └── 574
        │   │   │   │   │   └── 566
        │   │   │   │   │       ├── 567
        │   │   │   │   │       └── 564
        │   │   │   │   └── 554
        │   │   │   │       ├── 560
        │   │   │   │       │   ├── 561
        │   │   │   │       │   └── 557
        │   │   │   │       └── 552
        │   │   │   │           ├── 553
        │   │   │   │           └── 547
        │   │   │   │               ├── 551
        │   │   │   │               └── 545
        │   │   │   └── 519
        │   │   │       ├── 526
        │   │   │       │   ├── 531
        │   │   │       │   │   ├── 533
        │   │   │       │   │   │   └── 536
        │   │   │       │   │   └── 528
        │   │   │       │   └── 522
        │   │   │       │       ├── 524
        │   │   │       │       └── 520
        │   │   │       │           └── 521
        │   │   │       └── 516
        │   │   │           ├── 517
        │   │   │           │   └── 518
        │   │   │           └── 514
        │   │   └── 483
        │   │       ├── 499
        │   │       │   ├── 507
        │   │       │   │   ├── 511
        │   │       │   │   │   └── 508
        │   │       │   │   └── 501
        │   │       │   │       ├── 504
        │   │       │   │       └── 500
        │   │       │   └── 492
        │   │       │       ├── 496
        │   │       │       └── 491
        │   │       │           └── 485
        │   │       └── 465
        │   │           ├── 470
        │   │           │   ├── 480
        │   │           │   │   └── 471
        │   │           │   └── 469
        │   │           └── 463
        │   │               └── 461
        │   └── 361
        │       ├── 399
        │       │   ├── 426
        │       │   │   ├── 443
        │       │   │   │   ├── 449
        │       │   │   │   │   ├── 456
        │       │   │   │   │   └── 448
        │       │   │   │   └── 432
        │       │   │   │       ├── 439
        │       │   │   │       │   ├── 442
        │       │   │   │       │   └── 436
        │       │   │   │       └── 431
        │       │   │   └── 413
        │       │   │       ├── 423
        │       │   │       │   ├── 424
        │       │   │       │   └── 414
        │       │   │       │       └── 416
        │       │   │       └── 403
        │       │   │           ├── 406
        │       │   │           │   ├── 411
        │       │   │           │   └── 404
        │       │   │           └── 402
        │       │   └── 383
        │       │       ├── 390
        │       │       │   ├── 392
        │       │       │   │   └── 395
        │       │       │   └── 388
        │       │       │       ├── 389
        │       │       │       └── 387
        │       │       └── 375
        │       │           ├── 379
        │       │           │   └── 376
        │       │           └── 373
        │       │               └── 365
        │       └── 325
        │           ├── 339
        │           │   ├── 352
        │           │   │   ├── 354
        │           │   │   │   ├── 355
        │           │   │   │   └── 353
        │           │   │   └── 347
        │           │   │       ├── 349
        │           │   │       │   ├── 351
        │           │   │       │   └── 348
        │           │   │       └── 340
        │           │   │           └── 346
        │           │   └── 329
        │           │       ├── 333
        │           │       │   └── 335
        │           │       └── 328
        │           └── 296
        │               ├── 310
        │               │   ├── 315
        │               │   │   ├── 319
        │               │   │   │   └── 317
        │               │   │   └── 313
        │               │   └── 301
        │               │       ├── 303
        │               │       │   ├── 305
        │               │       │   └── 302
        │               │       └── 297
        │               │           └── 298
        │               └── 275
        │                   ├── 287
        │                   │   ├── 290
        │                   │   │   └── 288
        │                   │   └── 279
        │                   └── 272
        │                       ├── 274
        │                       │   └── 273
        │                       └── 264
        └── 137
            ├── 221
            │   ├── 234
            │   │   ├── 238
            │   │   │   ├── 255
            │   │   │   │   ├── 259
            │   │   │   │   │   └── 258
            │   │   │   │   └── 248
            │   │   │   │       └── 240
            │   │   │   └── 236
            │   │   │       ├── 237
            │   │   │       └── 235
            │   │   └── 227
            │   │       ├── 230
            │   │       │   ├── 232
            │   │       │   └── 228
            │   │       │       └── 229
            │   │       └── 224
            │   │           ├── 225
            │   │           └── 222
            │   └── 185
            │       ├── 194
            │       │   ├── 210
            │       │   │   ├── 217
            │       │   │   │   ├── 218
            │       │   │   │   └── 214
            │       │   │   └── 204
            │       │   │       ├── 205
            │       │   │       └── 198
            │       │   └── 190
            │       │       ├── 192
            │       │       └── 189
            │       └── 172
            │           ├── 177
            │           │   ├── 181
            │           │   └── 174
            │           │       ├── 175
            │           │       └── 173
            │           └── 163
            │               ├── 167
            │               │   ├── 171
            │               │   │   └── 170
            │               │   └── 164
            │               └── 160
            │                   ├── 162
            │                   └── 149
            │                       ├── 150
            │                       └── 138
            └── 35
                ├── 96
                │   ├── 120
                │   │   ├── 128
                │   │   │   ├── 133
                │   │   │   │   ├── 136
                │   │   │   │   └── 132
                │   │   │   └── 123
                │   │   └── 110
                │   │       ├── 112
                │   │       │   ├── 116
                │   │       │   │   └── 117
                │   │       │   └── 111
                │   │       └── 102
                │   │           ├── 104
                │   │           │   └── 106
                │   │           └── 101
                │   │               └── 98
                │   └── 64
                │       ├── 85
                │       │   ├── 88
                │       │   │   ├── 93
                │       │   │   └── 86
                │       │   └── 72
                │       │       ├── 78
                │       │       │   ├── 83
                │       │       │   └── 74
                │       │       └── 71
                │       │           └── 66
                │       └── 44
                │           ├── 57
                │           │   ├── 60
                │           │   └── 48
                │           └── 38
                │               ├── 41
                │               │   └── 40
                │               └── 36
                └── 22
                    ├── 29
                    │   ├── 31
                    │   │   ├── 33
                    │   │   └── 30
                    │   └── 26
                    │       ├── 28
                    │       └── 24
                    └── 9
                        ├── 14
                        │   ├── 18
                        │   │   ├── 21
                        │   │   └── 17
                        │   └── 12
                        └── 2
                            ├── 5
                            │   └── 8
                            └── 1


    New Tree with Removed Numbers:
    483
    ├── 780
    │   ├── 922
    │   │   ├── 980
    │   │   └── 896
    │   │       └── 890
    │   └── 711
    │       └── 639
    └── 228
        ├── 328
        │   ├── 383
        │   └── 296
        └── 150
            ├── 190
            └── 2


    New Tree with Lopsided Injection:
    1014
    ├── 1030
    │   ├── 1038
    │   │   ├── 1042
    │   │   │   ├── 1046
    │   │   │   │   ├── 1048
    │   │   │   │   │   ├── 1049
    │   │   │   │   │   └── 1047
    │   │   │   │   └── 1044
    │   │   │   │       ├── 1045
    │   │   │   │       └── 1043
    │   │   │   └── 1040
    │   │   │       ├── 1041
    │   │   │       └── 1039
    │   │   └── 1034
    │   │       ├── 1036
    │   │       │   ├── 1037
    │   │       │   └── 1035
    │   │       └── 1032
    │   │           ├── 1033
    │   │           └── 1031
    │   └── 1022
    │       ├── 1026
    │       │   ├── 1028
    │       │   │   ├── 1029
    │       │   │   └── 1027
    │       │   └── 1024
    │       │       ├── 1025
    │       │       └── 1023
    │       └── 1018
    │           ├── 1020
    │           │   ├── 1021
    │           │   └── 1019
    │           └── 1016
    │               ├── 1017
    │               └── 1015
    └── 922
        ├── 1006
        │   ├── 1010
        │   │   ├── 1012
        │   │   │   ├── 1013
        │   │   │   └── 1011
        │   │   └── 1008
        │   │       ├── 1009
        │   │       └── 1007
        │   └── 1002
        │       ├── 1004
        │       │   ├── 1005
        │       │   └── 1003
        │       └── 1000
        │           ├── 1001
        │           └── 980
        └── 483
            ├── 780
            │   ├── 896
            │   │   └── 890
            │   └── 711
            │       └── 639
            └── 228
                ├── 328
                │   ├── 383
                │   └── 296
                └── 150
                    ├── 190
                    └── 2

        """
    main()
