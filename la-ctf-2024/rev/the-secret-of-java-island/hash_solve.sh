crunch 8 8 dp | while read -r line; do printf "%s " "$line"; printf %s "$line" | sha256sum; done | grep 4546af8bf66d0f1d13713d85d952f5de689e91092b23ed1634c984d3b8e960b3
