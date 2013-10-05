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
    'chibi_defines': [
      'SEXP_NO_INSTALL_H=1',  # TODO(bnoordhuis) Get rid of this.
      'sexp_default_module_path="/usr/local/lib"',
      'sexp_platform="<(OS)"',
      'sexp_release_name="carbon"',
      'sexp_so_extension="<(SHARED_LIB_SUFFIX)"',
      'sexp_version="0.6.1"',
    ],
    'chibi_stage0_sources': [
      'bignum.c',
      'eval.c',
      'gc.c',
      'opcodes.c',
      'sexp.c',
      'simplify.c',
      'vm.c',
    ],
  },

  'target_defaults': {
    'defines': ['<@(chibi_defines)']
  },

  'targets': [
    {
      'target_name': 'chibi-scheme-stage0',
      'type': 'executable',
      'dependencies': ['libchibi-scheme-stage0'],
      'sources': ['main.c'],
    },
    {
      'target_name': 'libchibi-scheme-stage0',
      'type': 'static_library',
      'include_dirs': ['include'],
      'direct_dependent_settings': {
        'include_dirs': ['include'],
        'defines': ['<@(chibi_defines)'],
      },
      'sources': ['<@(chibi_stage0_sources)'],
    },
    {
      'target_name': 'chibi-scheme',
      'type': 'executable',
      'dependencies': ['libchibi-scheme'],
      'sources': ['main.c'],
    },
    {
      'target_name': 'libchibi-scheme',
      'type': 'static_library',
      'dependencies': ['chibi-scheme-stage0'],
      'include_dirs': [
        'include',
        'lib/chibi',
        'lib/chibi/io',
      ],
      'direct_dependent_settings': {
        'include_dirs': ['include'],
        'defines': ['<@(chibi_defines)'],
      },
      'sources': [
        '<@(chibi_stage0_sources)',
        'lib/chibi/ast.c',
        'lib/chibi/disasm.c',
        'lib/chibi/heap-stats.c',
        'lib/chibi/optimize/profile.c',
        'lib/chibi/optimize/rest.c',
        'lib/chibi/weak.c',
        'lib/scheme/time.c',
        'lib/srfi/18/threads.c',
        'lib/srfi/27/rand.c',
        'lib/srfi/33/bit.c',
        'lib/srfi/33/bit.c',
        'lib/srfi/39/param.c',
        'lib/srfi/69/hash.c',
        'lib/srfi/95/qsort.c',
        'lib/srfi/98/env.c',
        '<(SHARED_INTERMEDIATE_DIR)/filesystem.c',
        '<(SHARED_INTERMEDIATE_DIR)/io.c',
        '<(SHARED_INTERMEDIATE_DIR)/net.c',
        '<(SHARED_INTERMEDIATE_DIR)/process.c',
        '<(SHARED_INTERMEDIATE_DIR)/stty.c',
        '<(SHARED_INTERMEDIATE_DIR)/system.c',
        '<(SHARED_INTERMEDIATE_DIR)/time-gen.c',  # Work around basename clash.
      ],
      'actions': [
        {
          'action_name': 'filesystem.c',
          'inputs': ['lib/chibi/filesystem.stub'],
          'outputs': ['<(SHARED_INTERMEDIATE_DIR)/filesystem.c'],
          'action': [
            '<(PRODUCT_DIR)/chibi-scheme-stage0',
            'tools/chibi-ffi',
            '<@(_inputs)',
            '<@(_outputs)'
          ]
        },
        {
          'action_name': 'io.c',
          'inputs': ['lib/chibi/io/io.stub'],
          'outputs': ['<(SHARED_INTERMEDIATE_DIR)/io.c'],
          'action': [
            '<(PRODUCT_DIR)/chibi-scheme-stage0',
            'tools/chibi-ffi',
            '<@(_inputs)',
            '<@(_outputs)'
          ]
        },
        {
          'action_name': 'net.c',
          'inputs': ['lib/chibi/net.stub'],
          'outputs': ['<(SHARED_INTERMEDIATE_DIR)/net.c'],
          'action': [
            '<(PRODUCT_DIR)/chibi-scheme-stage0',
            'tools/chibi-ffi',
            '<@(_inputs)',
            '<@(_outputs)'
          ]
        },
        {
          'action_name': 'process.c',
          'inputs': ['lib/chibi/process.stub'],
          'outputs': ['<(SHARED_INTERMEDIATE_DIR)/process.c'],
          'action': [
            '<(PRODUCT_DIR)/chibi-scheme-stage0',
            'tools/chibi-ffi',
            '<@(_inputs)',
            '<@(_outputs)'
          ]
        },
        {
          'action_name': 'stty.c',
          'inputs': ['lib/chibi/stty.stub'],
          'outputs': ['<(SHARED_INTERMEDIATE_DIR)/stty.c'],
          'action': [
            '<(PRODUCT_DIR)/chibi-scheme-stage0',
            'tools/chibi-ffi',
            '<@(_inputs)',
            '<@(_outputs)'
          ]
        },
        {
          'action_name': 'system.c',
          'inputs': ['lib/chibi/system.stub'],
          'outputs': ['<(SHARED_INTERMEDIATE_DIR)/system.c'],
          'action': [
            '<(PRODUCT_DIR)/chibi-scheme-stage0',
            'tools/chibi-ffi',
            '<@(_inputs)',
            '<@(_outputs)'
          ]
        },
        {
          'action_name': 'time-gen.c',
          'inputs': ['lib/chibi/time.stub'],
          'outputs': ['<(SHARED_INTERMEDIATE_DIR)/time-gen.c'],
          'action': [
            '<(PRODUCT_DIR)/chibi-scheme-stage0',
            'tools/chibi-ffi',
            '<@(_inputs)',
            '<@(_outputs)'
          ]
        },
      ]
    }
  ]
}
