# Copyright 2020 Paul Lu
# ------------------------------------------------------------
# Name: Krish Gandhi
# ID: 1621641
# CMPUT 274, Fall 2020
#
# Assignment #2: Huffman Coding
# ------------------------------------------------------------
import bitio
import huffman
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''

    tree = pickle.load(tree_stream)

    return tree


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """

    # traverse the tree until a leaf is found
    while True:
        # read in the next bit
        single_bit = bitreader.readbit()

        # if 0, then go down the left branch,
        # else (1) go down right branch
        if single_bit == 0:
            tree = tree.getLeft()
        else:
            tree = tree.getRight()

        # break from while loop if leaf is found
        if isinstance(tree, huffman.TreeLeaf):
            break

    # return single byte representing the next character
    return tree.getValue()


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''

    # create a huffman tree
    tree = read_tree(compressed)

    bitread = bitio.BitReader(compressed)
    bitwrite = bitio.BitWriter(uncompressed)

    # write to 'uncompressed' stream until EOF is reached
    while True:
        decode = decode_byte(tree, bitread)

        if decode is not None:
            # write decoded symbol with 8 bits
            bitwrite.writebits(decode, 8)
        else:
            break

    return


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''

    pickle.dump(tree, tree_stream)

    return


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''

    # write tree to 'compressed' stream
    write_tree(tree, compressed)

    # create dictionary, where each key [byte (leaf node)] corresponds
    # to a value [bit sequence]
    encoded_table = huffman.make_encoding_table(tree)

    bitread = bitio.BitReader(uncompressed)
    bitwrite = bitio.BitWriter(compressed)

    # write to 'compressed' stream until EOF is reached
    while True:

        try:
            # read in 8 bits
            byte = bitread.readbits(8)

            # find corressponding bit sequence (tuple of True and False)
            bit_sequence = encoded_table[byte]

            # write encoded bit_sequence, bitwise
            for bit in bit_sequence:
                bitwrite.writebit(bit)

        except EOFError:
            # write None to indicate EOF to decompressor
            bit_sequence = encoded_table[None]
            for bit in bit_sequence:
                bitwrite.writebit(bit)

            break

    bitwrite.flush()

    return
