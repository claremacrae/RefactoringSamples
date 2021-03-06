#!/usr/bin/env bash

# ---------------------------------------------------
# Update code examples
# ---------------------------------------------------
# For info on mdsnippets, see https://github.com/SimonCropp/MarkdownSnippets

# install dotnet SDK from http://go.microsoft.com/fwlink/?LinkID=798306&clcid=0x409
# Then install MarkdownSnippets.Tool with
#   dotnet tool install -g MarkdownSnippets.Tool
# To update:
#   dotnet tool update  -g MarkdownSnippets.Tool
# To uninstall (e.g. to downgrade to a lower version)
# dotnet tool uninstall -g MarkdownSnippets.Tool

#
#   See https://github.com/approvals/ApprovalTests.cpp/blob/master/doc/BuildingDocumentation.md#top
#dotnet tool update  -g MarkdownSnippets.Tool --version 23.0.0 || exit
mdsnippets || exit 1
