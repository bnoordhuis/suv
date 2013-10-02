# Copyright (c) 2013, Ben Noordhuis <info@bnoordhuis.nl>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

{
  'variables': {
    'sexp_default_module_path%': '/usr/local/lib',
    'sexp_platform%': '<(OS)',
    'sexp_release_name': 'carbon',
    'sexp_so_extension%': '<(SHARED_LIB_SUFFIX)',
    'sexp_version': '0.6.1',
  },

  'target_defaults': {
    'defines': [
      'SEXP_NO_INSTALL_H=1',
      'sexp_default_module_path="<(sexp_default_module_path)"',
      'sexp_platform="<(sexp_platform)"',
      'sexp_release_name="<(sexp_release_name)"',
      'sexp_so_extension="<(sexp_so_extension)"',
      'sexp_version="<(sexp_version)"',
    ],
  },

  'targets': [
    {
      'target_name': 'chibi-scheme',
      'type': 'executable',
      'sources': ['main.c'],
      'dependencies': ['libchibi-scheme'],
    },
    {
      'target_name': 'libchibi-scheme',
      'type': 'static_library',
      'include_dirs': ['include'],
      'direct_dependent_settings': {
        'include_dirs': ['include'],
        'defines': [
          'SEXP_NO_INSTALL_H=1',
          'sexp_default_module_path="<(sexp_default_module_path)"',
          'sexp_platform="<(sexp_platform)"',
          'sexp_release_name="<(sexp_release_name)"',
          'sexp_so_extension="<(sexp_so_extension)"',
          'sexp_version="<(sexp_version)"',
        ],
      },
      'sources': [
        'bignum.c',
        'eval.c',
        'gc.c',
        'opcodes.c',
        'sexp.c',
        'simplify.c',
        'vm.c',
      ],
    }
  ]
}
