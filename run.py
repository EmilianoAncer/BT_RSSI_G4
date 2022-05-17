#!/usr/bin/env python3
"""Shbang."""
import gather


def main():
    """Use functions of gather.py here"""
    positions = gather.get_full_object()
    # gather.print_positions(positions, 3)
    gather.print_data_to_file(positions)

main()
