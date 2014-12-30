#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""For homework CH4 P22 and P23 in the textbook."""

from numpy import Inf

def check(dist):
    for start in dist:
        for end in dist[start]:
            if dist[start][end] != dist[end][start]:
                print start, "and", end, "are not paired"

def dijkstra(start, dist, nodes, order):
    print '-------------------------'
    print 'start: ', start

    result = {}
    counter = 0

    # step 0
    for n in nodes:
        dist[n][n] = 0
        result[n] = [dist[start][n], start] if n in dist[start] else [Inf, start]

    checked = set(start)

    def print_track():
        print counter, '[%s]' % ' '.join(c for c in checked),
        print ' '.join(n + ' ' + str(result[n]) for n in order)
        counter += 1

    print_track()  # step 0

    while checked != set(nodes):
        next_node = min((n for n in result if n not in checked),
                        key=lambda x:result[x][0])
        print 'add', next_node
        start_to_next = result[next_node][0]
        for neighbor in dist[next_node]:
            next_to_neigh = dist[next_node][neighbor]
            if start_to_next + next_to_neigh < result[neighbor][0]:
                result[neighbor][0] = start_to_next + next_to_neigh
                result[neighbor][1] = next_node
        checked.add(next_node)
        print_track()


def main():
    dist = {
        'x': { 'y': 6, 'v': 8, 'w': 6},
        'y': { 'x': 6, 'z': 12, 'v': 1, 't': 9},
        'v': { 'x': 8, 'w': 4, 'u': 3, 't': 4, 'y': 1},
        't': { 'z': 5, 'y': 9, 'v': 4, 'u': 2, 's': 1},
        'u': { 'w': 8, 's': 4, 't': 2, 'v': 3},
        'w': { 'u': 8, 'v': 4, 'x': 6},
        'z': { 'y': 12, 't': 5},
        's': {'u': 4, 't': 1}
    }
    nodes = ['x', 'y', 'z', 'u', 'v', 'w', 't', 's']

    dijkstra('x', dist, nodes, ['s', 't', 'u', 'v', 'w', 'y', 'z'])
    dijkstra('s', dist, nodes, ['t', 'u', 'v', 'w', 'x', 'y', 'z'])
    dijkstra('t', dist, nodes, ['s', 'u', 'v', 'w', 'x', 'y', 'z'])
    dijkstra('u', dist, nodes, ['s', 't', 'v', 'w', 'x', 'y', 'z'])
    dijkstra('v', dist, nodes, ['s', 't', 'u', 'w', 'x', 'y', 'z'])
    dijkstra('w', dist, nodes, ['s', 't', 'u', 'v', 'x', 'y', 'z'])
    dijkstra('y', dist, nodes, ['s', 't', 'u', 'v', 'w', 'x', 'z'])
    dijkstra('z', dist, nodes, ['s', 't', 'u', 'v', 'w', 'x', 'y'])


    # This is for the 5th edition of the text book
    dist2 = {
        'x': { 'y': 6, 'z': 8, 'v': 3, 'w': 6},
        'y': { 'x': 6, 'z': 12, 'v': 8, 't': 7},
        'v': { 'x': 3, 'w': 4, 'u': 3, 't': 4, 'y': 8},
        't': { 'y': 7, 'v': 4, 'u': 2},
        'u': { 'w': 3, 't': 2, 'v': 3},
        'w': { 'u': 3, 'v': 4, 'x': 6},
        'z': { 'y': 12, 'x': 8}
    }
    nodes2 = ['x', 'y', 'z', 'u', 'v', 'w', 't']
    order2 = ['t', 'u', 'v', 'w', 'x', 'y', 'z']

if __name__ == "__main__":
    main()

